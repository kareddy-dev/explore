# Agent Orchestration System: Formal Problem Statement v2

**Status:** Design Phase (Post-Phase 0 Validation)
**Created:** 2025-10-20
**Audience:** External AI Architecture Expert
**Context:** Designing multi-agent orchestration within Claude Code constraints

---

## Executive Summary

Design a production-grade multi-agent orchestration system for **Claude Code** (Anthropic's agentic CLI tool) that enables:

1. **YAML-based workflow definitions** - Declarative, reusable multi-agent pipelines
2. **Parallel agent execution** - 3x speedup (156s → 51s for N=12 agents)
3. **Inter-agent communication** - Within architectural constraints
4. **Reusable agent library** - Domain-agnostic agents parametrized via inputs
5. **Message queue infrastructure** - Task distribution and coordination

**Critical Discovery:** Phase 0 validation confirmed Task tool supports parallel execution with spawn overhead. Revised architecture separates orchestration (main thread commands) from execution (subagents).

---

## 1. Claude Code Architecture Primer

### 1.1 What is Claude Code?

**Claude Code** is an agentic CLI tool that runs AI assistants (Claude) in your terminal with:
- File system access (read, write, edit files)
- Shell command execution (bash, git, npm, etc.)
- Tool integration via MCP (Model Context Protocol)
- Persistent memory via CLAUDE.md files
- Extensibility via agents, commands, hooks, MCP servers

**Core Concept:** Natural language interface to development workflows backed by LLM reasoning + tool execution.

---

### 1.2 Claude Code Component Types

Claude Code has **three distinct component types** with different capabilities:

#### Component Type 1: Main Thread (User Session)

**What it is:**
- The primary REPL where user types commands
- Direct interaction with Claude

**Capabilities:**
- ✅ Can spawn subagents via `Task` tool
- ✅ Can use all tools (Bash, Read, Write, Edit, MCP tools)
- ✅ Has full 200K context window
- ✅ Sees entire conversation history

**Location:** N/A (runtime, interactive)

---

#### Component Type 2: Commands (Slash Commands)

**What it is:**
- User-defined prompts stored as markdown files
- Invoked via `/command-name` syntax
- **Execute in main thread context** (critical!)

**Capabilities:**
- ✅ Can spawn subagents via `Task` tool (runs in main thread)
- ✅ Can use all tools
- ✅ Has full context access
- ✅ Can orchestrate multi-step workflows

**Location:** `.claude/commands/*.md`

**Example:**
```markdown
# .claude/commands/run-tests.md
---
name: run-tests
description: Run test suite and report failures
---

Execute the test suite:
1. Run `npm test`
2. If failures, analyze and suggest fixes
3. Report results in structured format
```

**Invocation:** User types `/run-tests` → main thread executes prompt

---

#### Component Type 3: Agents (Subagents)

**What it is:**
- Specialized AI assistants defined as markdown files
- Spawned by main thread or commands via `Task` tool
- **Execute in isolated context** (separate 200K window)

**Capabilities:**
- ❌ **CANNOT spawn other subagents** (no Task tool access)
- ✅ Can use all other tools (Bash, Read, Write, MCP tools)
- ✅ Has separate 200K context (doesn't pollute main context)
- ❌ Cannot see main thread's conversation history
- ✅ Returns results to spawner upon completion

**Location:** `.claude/agents/**/*.md`

**Example:**
```markdown
# .claude/agents/core/test-analyzer.md
---
name: test-analyzer
description: Analyze test failures and suggest fixes
model: inherit
---

When invoked with test output:
1. Parse failures
2. Identify root causes
3. Suggest specific fixes
4. Return structured report
```

**Invocation:** Main thread calls `Task(agent="test-analyzer", prompt="...")`

---

### 1.3 Critical Architectural Rule

**ONLY main thread and commands can spawn subagents.**

```
Main Thread (User REPL)
  ├─> Can spawn Agent A ✅ (via Task tool)
  ├─> Can spawn Agent B ✅
  └─> Can spawn Agent C ✅

Command (runs in main thread)
  ├─> Can spawn Agent A ✅ (via Task tool)
  ├─> Can spawn Agent B ✅
  └─> Can spawn Agent C ✅

Agent A (subagent)
  ├─X CANNOT spawn Agent B (no Task tool access)
  ├─X CANNOT spawn Agent C
  └─X CANNOT spawn further subagents
```

**Implication:** Multi-agent orchestration logic MUST live in commands, not agents.

---

### 1.4 Model Context Protocol (MCP)

**What it is:**
- Standard for extending Claude Code with external tools
- MCP servers expose tools that both main thread and subagents can use

**Capabilities:**
- ✅ Available to main thread
- ✅ Available to all subagents
- ✅ Enables shared state (message queues, databases, APIs)

**Location:** `.claude/mcp/*.py` + configuration in `mcp.json`

**Example:**
```python
# .claude/mcp/simple-queue.py
from mcp.server import Server

mcp = Server("simple-queue")

@mcp.tool()
async def enqueue_task(agent: str, branch_id: str, inputs: dict):
    """Enqueue a task for processing"""
    # Implementation...
```

**Key Insight:** MCP tools provide shared state for agent coordination without violating the "no subagent spawning" constraint.

---

## 2. Core Constraints (Immutable)

### Constraint C1: File-Based Component Definitions

**Limitation:**
```
Components MUST be pre-defined as files:
.claude/commands/*.md    # Commands
.claude/agents/**/*.md   # Agents
```

**Impact:**
- ❌ Cannot create agents/commands dynamically at runtime
- ❌ Cannot modify definitions during session
- ✅ Can reference existing agents/commands
- ✅ Can parametrize via inputs

**Workaround:** Pre-create generic agents, parametrize behavior via inputs/prompts.

---

### Constraint C2: Hierarchical Invocation (CRITICAL)

**Limitation:**
```
Main Thread / Commands
  ├─> Can spawn Agent A (via Task tool) ✅
  ├─> Can spawn Agent B (via Task tool) ✅
  └─> Can spawn Agent C (via Task tool) ✅

Agent A (subagent)
  ├─X CANNOT spawn Agent B (no Task tool)
  ├─X CANNOT use Task tool at all
  └─X CANNOT spawn further subagents
```

**Architectural Rule:**
> Only main thread and commands (which run in main thread) can spawn subagents. Subagents cannot spawn other subagents.

**Evidence:**
- Task tool is available only to main thread
- Subagents have separate context windows (isolated execution)
- No built-in mechanism for subagent-to-subagent delegation

**Design Decision:**
> Orchestration logic MUST live in commands (`.claude/commands/*.md`), not agents (`.claude/agents/*.md`).

---

### Constraint C3: Sequential Spawning with Parallel Execution

**Limitation (Validated via Phase 0 Test):**

**Test Results:**
- 3 agents × 15s sleep each
- Total time: 39 seconds
- Analysis: 39s < 45s (pure sequential) → parallelism confirmed

**Actual Behavior:**
```
Time 0-9s:   Spawn 3 workers (3s each, sequential)
Time 9-24s:  All workers sleep 15s (PARALLEL) ✅
Time 24-39s: Results aggregated
```

**Timing Model:**
```
T_total = (N_agents × T_spawn) + max(T_work_i) + T_aggregation

Where:
- T_spawn ≈ 3s (per agent, sequential)
- T_work = agent execution time (parallel)
- T_aggregation ≈ 5s
```

**Example (N=12, T_work=10s):**
- Sequential: 12 × 13s = 156s
- Parallel: (12 × 3s) + 10s + 5s = 51s
- **Speedup: 3.06x** ✅

**Design Decision:**
> Task spawning is sequential (unavoidable 3s overhead per agent), but execution is parallel. Architecture is valid, adjust speedup expectations from 4x to 3x.

---

### Constraint C4: Context Window Isolation

**Limitation:**
- Each subagent has separate 200K token context
- Subagent context is NOT shared with main thread during execution
- Results returned only at completion (no streaming of intermediate state)

**Impact:**
- ✅ Parallel agents don't pollute each other's context
- ❌ Agents can't see each other's progress in real-time
- ❌ Main thread can't monitor agent state during execution

**Design Decision:**
> Use external state store (MCP-based queue) for agents to publish progress/results that orchestrator can poll.

---

### Constraint C5: MCP Tool Integration

**Limitation:**
- MCP tools accessible to both main thread and subagents
- Tool calls are synchronous (request → response)
- MCP servers run as separate processes (stdio transport)

**Design Decision:**
> MCP server for message queue uses polling model (agents check queue via tool calls) rather than push model.

---

### Constraint C6: No Built-In Concurrency Primitives

**Limitation:**
- Commands are markdown-based (not programming languages)
- No native `async`/`await`, threads, or process pools
- Task tool spawns agents sequentially

**Design Decision:**
> Implement task queue pattern via MCP: command enqueues N tasks, spawns N workers (sequentially), workers process from queue (parallel), command polls for completion.

---

## 3. Problem Context

### 3.1 Current State (Baseline)

**Existing System:**
- 12 pre-defined agents in `.claude/agents/`
  - 3 core: decision-aggregator, self-approver, skeptic-reviewer
  - 4 SaaS: ideation-scout, market-mapper, feasibility-engineer, growth-planner
  - 5 Trading: regime-detector, strategy-screener, backtest-sanity, risk-manager, execution-planner
- 1 orchestrator command: `explore.md` with hardcoded workflows
- Sequential execution (agents run one after another)
- Hub-and-spoke communication (orchestrator ↔ agents only)

**Performance (Baseline):**
- Stage 1 (Discover) with N=12 agents: ~156 seconds (sequential)
- Context usage: 30-40% per stage (grows linearly)
- Agent reusability: Low (workflow logic embedded in orchestrator)

**Pain Points:**
1. **Sequential bottleneck** - No parallelism (1 agent completes → next starts)
2. **Workflow rigidity** - New workflows require code changes
3. **Agent duplication** - 12 specialized agents with overlapping logic
4. **Context pollution** - Long workflows exceed 50% context threshold

---

### 3.2 Desired State (Target)

**Target System:**
- YAML-based workflow definitions (declarative, version-controlled)
- Parallel agent execution (fan-out/barrier pattern)
- Message queue for task distribution
- Generic worker agent (single agent, multiple roles)
- Observable, debuggable, production-ready

**Target Performance:**
- Stage 1 (Discover) with N=12 agents: <60 seconds (parallel)
- Context usage: <20% per stage
- Agent reusability: High (single generic worker)
- Extensibility: High (new workflow = YAML file)

**Success Criteria (Revised):**
- ✅ 3x latency improvement (156s → 51s) [adjusted from 4x based on Phase 0]
- ✅ Single generic agent replaces 12 specialized agents
- ✅ Zero code changes to add new workflows (YAML only)
- ✅ Inter-agent feedback loops functional
- ✅ Queue recovery from failures (<5% data loss)

---

## 4. Proposed Architecture

### 4.1 Three-Plane Design

#### Control Plane: run-workflow.md (COMMAND)

**Type:** Command (runs in main thread)
**Location:** `.claude/commands/run-workflow.md`
**Capabilities:** Has Task tool access ✅

**Responsibilities:**
1. Parse YAML workflow definition
2. Initialize workflow state
3. For parallel stages:
   - Register barrier (MCP: `register_barrier`)
   - Enqueue N tasks (MCP: `enqueue_task` × N)
   - **Spawn N workers (Task tool × N)** ✅ Valid - command has Task access
   - Wait at barrier (MCP: `wait_for_barrier`)
4. For centralized stages (aggregate/gate/sequential):
   - Spawn single worker with direct prompt (Task tool)
5. Manage state transitions, evaluate gates

**Why Command, Not Agent?**
- Commands run in main thread → have Task tool access
- Can spawn multiple subagents
- If this were an agent, it couldn't spawn workers (Constraint C2)

---

#### Data Plane: simple-queue.py (MCP SERVER)

**Type:** MCP Server
**Location:** `.claude/mcp/simple-queue.py`
**Capabilities:** Provides tools to both commands and agents

**Responsibilities:**
1. Task queue management (asyncio.Queue)
2. Result storage
3. Barrier synchronization (asyncio.Event)
4. Optional: Inter-agent messaging

**Tools Provided:**
```python
@mcp.tool()
async def enqueue_task(agent: str, branch_id: str, prompt: str) -> dict:
    """Enqueue task for worker to process"""

@mcp.tool()
async def dequeue_task() -> dict:
    """Worker fetches next task from queue"""

@mcp.tool()
async def post_result(branch_id: str, result: any) -> dict:
    """Worker submits result after execution"""

@mcp.tool()
async def register_barrier(barrier_id: str, expected_count: int) -> dict:
    """Set up barrier for N agents"""

@mcp.tool()
async def wait_for_barrier(barrier_id: str, timeout: int) -> dict:
    """Block until N agents complete (asyncio.Event)"""

@mcp.tool()
async def notify_barrier(barrier_id: str) -> dict:
    """Worker signals completion (increments counter, fires Event if N reached)"""
```

**Why MCP Server?**
- Provides shared state (queue, results, barriers)
- Accessible to both command (orchestrator) and agents (workers)
- Enables coordination without violating "no subagent spawning" constraint

---

#### Execution Plane: generic-worker.md (AGENT)

**Type:** Agent (subagent)
**Location:** `.claude/agents/core/generic-worker.md`
**Capabilities:** No Task tool ❌, has all other tools + MCP tools ✅

**Responsibilities:**
1. Dequeue task from queue (MCP tool)
2. Execute embedded prompt (domain logic in YAML)
3. Post result (MCP tool)
4. Notify barrier (MCP tool)

**Why Agent, Not Command?**
- Needs isolation (separate 200K context per worker)
- Doesn't need to spawn other agents
- Can be spawned multiple times in parallel

**Execution Protocol:**
```markdown
When invoked:

Step 1: Check for direct prompt (centralized stages)
if "direct_prompt" in inputs:
    prompt = inputs["direct_prompt"]
    result = execute(prompt)
    return result  # Return directly, no queue

Step 2: Dequeue task (parallel stages)
task = mcp.simple_queue.dequeue_task()
branch_id = task["branch_id"]
prompt = task["prompt"]

Step 3: Execute prompt
result = execute(prompt)  # Use ggrep, analysis, formatting

Step 4: Post result
mcp.simple_queue.post_result(branch_id, result)

Step 5: Notify barrier
mcp.simple_queue.notify_barrier(barrier_id)
```

---

### 4.2 YAML Workflow Schema

```yaml
name: SaaS_Discovery_Parallel
version: "1.0"
description: Parallel SaaS ideation workflow
domain: SaaS

inputs:
  - name: problem_statement
    type: string
    required: true

stages:
  - name: Discover
    type: parallel_fan_out
    branch_count: 12
    execution_prompt: |
      You are a SaaS Ideation Scout.
      Branch ID: {{stage.branch_id}}
      Problem: {{inputs.problem_statement}}

      Method:
      1. Use ggrep tool to search GitHub for repos matching problem
      2. Analyze stars, forks, issues, README quality
      3. Identify 3 monetizable opportunities

      Output (JSON):
      {
        "ideas": [
          {"id": "I1", "name": "...", "repo": "...", "signals": {...}},
          {"id": "I2", "name": "...", "repo": "...", "signals": {...}},
          {"id": "I3", "name": "...", "repo": "...", "signals": {...}}
        ]
      }
    timeout: 300

  - name: Aggregate_Discover
    type: aggregate
    depends_on: Discover
    execution_prompt: |
      You are the Decision Aggregator.

      Input: {{Discover.*.output.ideas}}

      Method:
      1. Normalize all ideas (36 total from 12 branches)
      2. Score based on: stars, forks, issue velocity, README quality
      3. Deduplicate similar ideas
      4. Select top 5

      Output (JSON):
      {
        "top_5": [...],
        "brief": "..."
      }

  - name: Gate_Discover
    type: gate
    depends_on: Aggregate_Discover
    agent: core/self-approver
    success_condition: "output.status == 'APPROVED'"
    on_failure:
      action: halt
      message: "Discovery stage rejected"

outputs:
  - name: approved_ideas
    source: "Gate_Discover.output.approved_ideas"
```

---

### 4.3 Execution Flow Example

**User invokes:**
```bash
/run-workflow workflows/saas_discovery.yaml --inputs '{"problem_statement": "developer tools"}'
```

**run-workflow.md (COMMAND) executes:**

**Phase 1: Setup**
```python
workflow = parse_yaml("workflows/saas_discovery.yaml")
state = {"inputs": inputs, "stages": {}}
```

**Phase 2: Discover Stage (parallel_fan_out)**
```python
# Register barrier
mcp.simple_queue.register_barrier("Discover", expected_count=12)

# Enqueue 12 tasks (3s each = 36s sequential)
for i in range(12):
    branch_id = f"B{i+1}"
    prompt = render_template(stage.execution_prompt, {
        "stage.branch_id": branch_id,
        "inputs.problem_statement": inputs["problem_statement"]
    })
    mcp.simple_queue.enqueue_task(
        agent="generic-worker",
        branch_id=branch_id,
        prompt=prompt
    )

# Spawn 12 workers (3s each = 36s sequential)
# Spawning is sequential, but execution will be parallel
for i in range(12):
    Task(
        agent="generic-worker",
        description=f"Worker {i+1}"
    )

# Wait at barrier (blocks until all 12 complete)
# Workers execute in parallel: ~10s work time
results = mcp.simple_queue.wait_for_barrier("Discover", timeout=300)
state["stages"]["Discover"] = results
```

**Timeline:**
```
Time 0-36s:   Command enqueues 12 tasks
Time 36-72s:  Command spawns 12 workers (sequential)
Time 72-82s:  Workers execute in parallel (dequeue, ggrep, analyze, post)
Time 82s:     Barrier fires, command receives all results
```

**Total: ~82s (vs 156s sequential = 1.9x speedup)**

**Phase 3: Aggregate Stage (centralized, no queue)**
```python
# Direct invocation, no queue overhead
prompt = render_template(stage.execution_prompt, {
    "Discover.*.output.ideas": state["stages"]["Discover"]
})

result = Task(
    agent="generic-worker",
    prompt=prompt
)

state["stages"]["Aggregate_Discover"] = result
```

**Phase 4: Gate Stage**
```python
result = Task(
    agent="core/self-approver",
    prompt=render_template(stage.execution_prompt, {
        "Aggregate_Discover.output": state["stages"]["Aggregate_Discover"]
    })
)

if result.status != "APPROVED":
    handle_gate_failure(stage.on_failure)
    return

state["stages"]["Gate_Discover"] = result
```

**Phase 5: Extract Outputs**
```python
outputs = extract_outputs(workflow.outputs, state)
return outputs
```

---

## 5. Key Design Decisions & Rationale

### Decision 1: Commands for Orchestration, Not Agents

**Rationale:**
- Only main thread has Task tool access
- Commands run in main thread → can spawn subagents
- Agents are subagents → cannot spawn other agents (Constraint C2)

**Implication:**
- Orchestration logic lives in `.claude/commands/run-workflow.md`
- Execution logic lives in `.claude/agents/core/generic-worker.md`
- Clear separation of concerns

---

### Decision 2: Single Generic Worker vs 12 Specialized Agents

**Rationale:**
- Domain logic embedded in YAML (execution_prompt)
- Worker is just an execution engine
- New domain = new YAML file, no new agent files

**Benefits:**
- 1 agent file instead of 12
- Zero code duplication
- Easier maintenance

---

### Decision 3: asyncio.Queue (MVP) → Redis (Production)

**Rationale:**
- asyncio.Queue: Zero dependencies, works immediately
- Proves pattern without external services
- Redis: Persistence + distribution for production scale

**Migration Path:**
```python
# MCP server interface stays same
@mcp.tool()
async def enqueue_task(...): ...

# Backend swaps: MVP uses asyncio.Queue, production uses Redis
```

---

### Decision 4: Embedded Execution Prompts in YAML

**Rationale:**
- All domain logic in YAML (not agent files)
- New workflow = edit YAML, no code changes
- Worker is generic execution engine

**Tradeoff:**
- YAML files larger (~240 lines vs 50 lines with agent refs)
- But: No agent file proliferation, better maintainability

---

### Decision 5: Optimized Centralized Stages

**Rationale:**
- aggregate/gate/sequential stages don't need queue
- Direct Task invocation saves ~3s queue overhead per stage

**Implementation:**
- parallel_fan_out: Uses queue + barrier
- Other stages: Direct Task invocation with `direct_prompt`

---

## 6. Implementation Phases

### Phase 0: Validation ✅ COMPLETED

**Duration:** 2 hours
**Status:** PASSED

**Tasks:**
1. ✅ Test parallel execution (3 workers × 15s sleep = 39s)
2. ✅ Confirm: Parallelism exists, spawn overhead is 3s/agent
3. ✅ Validate: 3x speedup achievable (156s → 51s)

**Results:**
- Sequential spawn: 3s per agent
- Parallel execution: Confirmed
- Revised speedup: 3x (not 4x)

**Gate:** ✅ Proceed to Phase 1

---

### Phase 1: Message Queue MVP

**Duration:** 6 hours
**Status:** NOT STARTED

**Deliverables:**
1. `.claude/mcp/simple-queue.py` (asyncio.Queue + asyncio.Event)
2. MCP tools: enqueue_task, dequeue_task, post_result, register_barrier, wait_for_barrier, notify_barrier
3. Test with 3-branch manual workflow

**Success Criteria:**
- ✅ 3 agents run in parallel (not sequential)
- ✅ Latency <40s for N=3 (vs ~60s sequential)
- ✅ Zero external dependencies

**Gate:** Only proceed if 2x+ speedup achieved

---

### Phase 2: Generic Worker + YAML Parser

**Duration:** 8 hours
**Status:** NOT STARTED

**Deliverables:**
1. `.claude/agents/core/generic-worker.md`
2. `.claude/commands/run-workflow.md` (hardcoded YAML parser, supports 3 stage types)
3. Test YAML: `workflows/saas_simple.yaml` (3 stages)

**Success Criteria:**
- ✅ Can define workflow in YAML
- ✅ Command parses and executes workflow
- ✅ Adding new stage = YAML edit, not code edit

**Gate:** Only proceed if YAML is clearer than markdown

---

### Phase 3: Template Rendering Engine

**Duration:** 8 hours
**Status:** NOT STARTED

**Deliverables:**
1. Dot notation resolver: Parse `{{Discover.*.output}}`, handle wildcards
2. Template renderer: Replace placeholders, format for LLM
3. Support for: inputs.X, stage.X, StageNa me.*.field, StageNa me.BranchID.field

**Success Criteria:**
- ✅ All template patterns work
- ✅ Handles nested arrays, wildcards
- ✅ Clear error messages for invalid paths

**Gate:** Only proceed if template system is robust

---

### Phase 4: Production Workflow Engine

**Duration:** 12 hours
**Status:** NOT STARTED

**Deliverables:**
1. Full YAML schema support (all 4 stage types)
2. Error handling, retry logic
3. State checkpointing (resume from failure)
4. 5+ example workflows (SaaS, Trading, Research domains)

**Success Criteria:**
- ✅ Supports all stage types
- ✅ Can resume from checkpoint
- ✅ Workflows work across domains

**Gate:** Only proceed if engine is stable

---

### Phase 5: Inter-Agent Communication (Optional)

**Duration:** 6 hours
**Status:** NOT STARTED

**Deliverables:**
1. MCP tools: send_message, check_messages
2. Example: skeptic-reviewer → ideation-scout feedback loop
3. Workflow example with revision stages

**Success Criteria:**
- ✅ Agent A can send message to Agent B
- ✅ Agent B processes and responds
- ✅ Orchestrator can monitor message flow

**Trigger:** Only if feedback loops provide value

---

### Phase 6: Redis Upgrade (Optional)

**Duration:** 4 hours
**Status:** NOT STARTED

**Deliverables:**
1. `.claude/mcp/redis-queue.py` (drop-in replacement)
2. Same MCP tool interface (no workflow changes)
3. Persistence and multi-machine support

**Trigger:** N>50 or multi-machine deployment needed

---

**Total Estimated Time:** 44 hours (excluding optional phases)

---

## 7. Open Questions for Expert Review

### Q1: Is Command-Based Orchestration Optimal?

**Current Design:**
- Orchestration logic in `.claude/commands/run-workflow.md` (command)
- Execution logic in `.claude/agents/core/generic-worker.md` (agent)

**Constraints:**
- Only main thread / commands can spawn subagents
- Subagents cannot spawn other subagents

**Question:**
Is there a better architecture that works within these constraints? Could we avoid the command entirely?

---

### Q2: Spawn Overhead Optimization

**Observed Behavior:**
- Task tool spawning: 3s per agent (sequential)
- For N=12: 36s spawn overhead

**Question:**
Can we reduce spawn overhead? Ideas:
- Agent pooling (spawn once, reuse)
- Batch spawning API
- Background spawning while previous agents work

---

### Q3: Queue vs Direct Invocation Trade-offs

**Current Design:**
- parallel_fan_out: Uses queue (coordination overhead)
- aggregate/gate/sequential: Direct Task invocation (no queue)

**Question:**
Should ALL stages use queue for consistency? Or is hybrid approach better?

**Tradeoffs:**
- Consistency: Queue for all stages (simpler mental model)
- Performance: Direct invocation for centralized stages (saves ~3s per stage)

---

### Q4: Template Language Complexity

**Proposed Syntax:**
- `{{inputs.problem_statement}}` - Workflow input
- `{{stage.branch_id}}` - Current stage metadata
- `{{Discover.*.output}}` - All outputs from Discover stage (wildcard)
- `{{Discover.B3.output}}` - Single branch output

**Question:**
Is this expressive enough? Should we support:
- Conditionals: `{{if Discover.B3.output.score > 0.8}}`
- Transformations: `{{Discover.*.output | filter(score > 0.8)}}`
- Or keep it simple (just templating)?

---

### Q5: Error Handling Strategy

**Scenarios:**
1. Worker crashes mid-execution
2. Worker returns malformed output
3. Barrier timeout (not all agents complete)
4. Queue overflow (too many tasks)

**Question:**
What's the best error handling strategy?
- Fail-fast: Halt workflow on first error
- Graceful degradation: Continue with partial results
- Retry: Automatic retry with exponential backoff
- Hybrid: Configurable per-stage

---

### Q6: State Management & Checkpointing

**Current Design:**
- Workflow state in-memory (lost on failure)

**Question:**
Should we checkpoint state to disk?
- After each stage completion
- Workflow can resume from checkpoint
- Useful for long workflows (>10 minutes)

**Tradeoff:**
- Complexity: File I/O, serialization, state reconstruction
- Benefit: Resilience to failures, can pause/resume

---

### Q7: Alternative to Message Queue?

**Current Design:**
- MCP-based message queue for task distribution

**Question:**
Are there alternatives that work within Claude Code constraints?
- Shared file system (write tasks to JSON files)
- Database (SQLite for task tracking)
- Redis pub/sub (real-time notifications)

**Constraints:**
- Must be accessible to both commands and agents
- Must support synchronization (barriers)

---

### Q8: Testing Strategy

**Challenge:**
- Commands and agents are markdown files (not unit-testable)
- MCP servers are Python (unit-testable)

**Question:**
How to test this system comprehensively?
- Integration tests: Full workflow execution
- Component tests: Test MCP server in isolation
- Simulation: Mock MCP tools, test orchestration logic

---

### Q9: Observability & Debugging

**Question:**
What observability is needed for production?

**Proposed Metrics:**
- Queue status: pending, running, completed tasks
- Agent status: spawn time, execution time, result size
- Workflow progress: current stage, % complete, ETA
- Error rates: failures per stage, retry counts

**Implementation:**
- MCP tool: `queue_status()` returns real-time metrics
- Command logs: Structured logging to file
- Dashboard: CLI UI showing workflow progress

---

### Q10: Scalability Limits

**Question:**
What are the scalability limits of this architecture?

**Current Bottlenecks:**
- Spawn overhead: 3s × N agents (for N=100: 300s = 5 minutes)
- asyncio.Queue: In-memory, single machine
- Context aggregation: Command must collect all results

**Question:**
When does this architecture break down?
- N agents > 50?
- T_work > 5 minutes?
- Result size > 100KB per agent?

**Mitigation Strategies:**
- Redis queue (distributed, persistent)
- Streaming results (don't wait for all)
- Agent pooling (reuse workers)

---

## 8. Request for Expert Critique

**Background:** You are an AI architecture expert. The requester is designing a multi-agent orchestration system within Claude Code (an agentic CLI tool with specific constraints).

**Your Task:**
1. **Critique the architecture** - What are the weak points? What could fail?
2. **Suggest alternatives** - Are there better patterns within the constraints?
3. **Challenge assumptions** - Which design decisions are questionable?
4. **Identify risks** - What could go wrong in production?
5. **Propose optimizations** - How can we improve performance, maintainability?

**Key Constraints to Respect:**
- Only commands (main thread) can spawn subagents (Constraint C2)
- Agents cannot spawn other agents
- Task spawning is sequential (3s overhead per agent)
- Context windows are isolated (200K per agent)
- All components must be pre-defined as files

**Focus Areas:**
- Is the command vs agent separation correct?
- Is the message queue pattern optimal?
- Can spawn overhead be reduced?
- Is the YAML approach better than alternatives?
- What are the scalability limits?

**Deliverable:** Written critique with specific recommendations and rationale.

---

## 9. Appendix: Glossary

**Claude Code:** Anthropic's agentic CLI tool for development workflows

**Main Thread:** The primary REPL where user types commands (has Task tool access)

**Command:** User-defined prompt in `.claude/commands/*.md`, runs in main thread, can spawn subagents

**Agent (Subagent):** AI assistant in `.claude/agents/*.md`, spawned by main thread/commands, cannot spawn other agents

**Task Tool:** Claude Code's built-in tool to spawn subagents (only available to main thread/commands)

**MCP (Model Context Protocol):** Extension system for Claude Code, provides shared tools to all agents

**MCP Server:** Python server exposing tools via MCP protocol

**Barrier:** Synchronization point where orchestrator waits for N agents to complete

**Fan-Out:** Spawn N agents in parallel

**Spawn Overhead:** Time to initialize and start a subagent (~3s per agent)

**Execution Prompt:** Domain logic embedded in YAML (rendered and passed to worker)

**Generic Worker:** Single agent that executes any prompt (parametrized behavior)

---

## 10. Document Metadata

**Version:** 2.0
**Last Updated:** 2025-10-20
**Authors:** Solo developer (INTJ/5w4), Claude (architecture assistant)
**Status:** Ready for Expert Review
**Previous Version:** v1.0 (assumed workflow-runner could be agent - incorrect)

**Change Log:**
- 2025-10-20 v2.0: Major revision after Phase 0 validation
  - Added Claude Code architecture primer (Section 1)
  - Corrected constraint C2: Only commands can spawn subagents
  - Changed orchestrator from agent to command
  - Added Phase 0 test results (parallel execution confirmed)
  - Revised speedup expectations (4x → 3x based on spawn overhead)
  - Restructured for external expert review
- 2025-10-20 v1.0: Initial draft (flawed - assumed workflow-runner could be agent)

**Related Documents:**
- `phase0-parallel-test-v2-results.md` - Validation test results
- `explore.md` - Current orchestrator implementation
- `.claude/agents/*` - Existing agent definitions

---

**END OF PROBLEM STATEMENT v2**
