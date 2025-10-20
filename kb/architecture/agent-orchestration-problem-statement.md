# Agent Orchestration System: Formal Problem Statement

**Status:** Design Phase
**Created:** 2025-10-20
**Domain:** Claude Code Multi-Agent Architecture
**Stakeholder:** Solo developer (INTJ/5w4)

---

## Executive Summary

Design and implement a production-grade agent orchestration system for Claude Code that enables:
1. **YAML-based workflow definitions** for reusable, declarative multi-agent pipelines
2. **Parallel agent execution** with sync barriers (4x speedup: 120s → 30s)
3. **Inter-agent communication** within architectural constraints
4. **Reusable agent library** applicable across problem domains (SaaS, Trading, Research, etc.)
5. **Message queue infrastructure** for task distribution and coordination

This system must work within Claude Code's file-based agent architecture while providing production-grade reliability, observability, and maintainability.

---

## 1. Problem Context

### 1.1 Current State (Baseline)

**Existing System:**
- 12 pre-defined agents in `.claude/agents/` directory
  - 3 core agents (decision-aggregator, self-approver, skeptic-reviewer)
  - 4 SaaS agents (ideation-scout, market-mapper, feasibility-engineer, growth-planner)
  - 5 Trading agents (regime-detector, strategy-screener, backtest-sanity, risk-manager, execution-planner)
- 1 orchestrator command (`explore.md`) with hardcoded workflows
- Sequential execution model (agents run one after another)
- Hub-and-spoke communication (orchestrator ↔ agents only)

**Performance Metrics:**
- Stage 1 (Discover) with N=12 branches: ~120 seconds (sequential)
- Context usage: 30-40% per stage (grows linearly)
- Agent reusability: Low (workflow logic embedded in orchestrator)
- Extensibility: Low (adding new workflow = rewrite explore.md)

**Pain Points:**
1. **Token inefficiency:** Orchestrator logic consumes 8K tokens per invocation
2. **Sequential bottleneck:** Agents can't run in parallel (1 agent completes → next starts)
3. **Workflow rigidity:** New workflows require code changes, not config changes
4. **Agent isolation:** No inter-agent communication (can't provide feedback loops)
5. **Context pollution:** Long workflows exceed 50% context threshold
6. **Maintenance burden:** Workflow logic scattered across 200+ lines of markdown

### 1.2 Desired State (Target)

**Target System:**
- YAML-based workflow definitions (declarative, version-controlled)
- Parallel agent execution (fan-out/barrier pattern)
- Message queue for task distribution
- Inter-agent communication within constraints
- Reusable agent library (domain-agnostic base agents)
- Observable, debuggable, production-ready

**Target Performance:**
- Stage 1 (Discover) with N=12 branches: <40 seconds (parallel)
- Context usage: <20% per stage (minimal orchestrator footprint)
- Agent reusability: High (agents work across domains)
- Extensibility: High (new workflow = YAML file, no code changes)

**Success Criteria:**
- ✅ 3x latency improvement (120s → 40s)
- ✅ 4x token reduction (8K → 2K orchestration overhead)
- ✅ Zero code changes to add new workflows
- ✅ Inter-agent feedback loops functional
- ✅ Queue recovery from failures (<5% data loss)
- ✅ Production-ready observability (queue status, agent state)

---

## 2. Core Constraints & Assumptions

### 2.1 Claude Code Architecture Constraints (Immutable)

#### **Constraint 1: File-Based Agent Definitions**

**Limitation:**
```markdown
# Agents MUST be pre-defined as files:
.claude/agents/
├── core/
│   └── my-agent.md
└── domain/
    └── specialized-agent.md
```

**Impact:**
- ❌ **Cannot create agents dynamically** (no runtime agent generation)
- ❌ **Cannot modify agent definitions at runtime** (file-based, immutable during session)
- ✅ **Can reference agents by path** (YAML workflows point to existing files)
- ✅ **Can pass different inputs** (parametrize existing agents)

**Workaround:**
- Use CLI `--agents` flag for session-specific agents (JSON format)
- Pre-create generic agents with configurable behavior via inputs

**Design Decision:**
> Build a **library of reusable generic agents** that can be parametrized via inputs, rather than creating new agent types dynamically.

---

#### **Constraint 2: Hierarchical Agent Invocation (Critical)**

**Limitation:**
```
Main Thread (Orchestrator)
  ├─> Can spawn Subagent A (via Task tool)
  ├─> Can spawn Subagent B (via Task tool)
  └─> Can spawn Subagent C (via Task tool)

Subagent A
  ├─X Cannot spawn Subagent B (no Task tool access)
  ├─X Cannot spawn Subagent C
  └─X Cannot spawn further subagents
```

**Architectural Rule:**
> **Only the main thread (orchestrator) can invoke subagents. Subagents cannot spawn other subagents.**

**Evidence:**
- Task tool is available only to main thread
- Subagents have separate context windows (isolated execution)
- No built-in mechanism for subagent-to-subagent delegation

**Impact on Communication:**
- ❌ **No peer-to-peer agent invocation** (Agent A can't call Agent B directly)
- ❌ **No agent chaining without orchestrator** (Agent A → Agent B requires orchestrator mediation)
- ❌ **No recursive subagent trees** (Subagent can't spawn sub-subagents)

**Design Decision:**
> Inter-agent communication must be **asynchronous and mediated** via shared state (message queue, shared memory), not direct invocation.

---

#### **Constraint 3: Context Window Isolation**

**Limitation:**
- Each subagent has separate 200K token context window
- Subagent context is NOT shared with main thread during execution
- Results are returned only at completion (no streaming of intermediate state)

**Impact:**
- ✅ Parallel agents don't pollute each other's context
- ❌ Agents can't see each other's progress in real-time
- ❌ Orchestrator can't monitor agent state during execution

**Design Decision:**
> Use **external state store** (Redis/asyncio.Queue) for agents to publish progress/results that orchestrator can poll.

---

### 2.2 Technical Constraints

#### **Constraint 4: MCP Tool Integration**

**Given:**
- Claude Code agents can use MCP tools
- MCP servers run as separate processes (stdio transport)
- Tool calls are synchronous (request → response)

**Limitation:**
- MCP tools can't maintain persistent connections to agents
- Each tool call is stateless
- No built-in pub/sub mechanism in MCP

**Design Decision:**
> MCP server for message queue must use **polling model** (agents check queue via tool calls) rather than push model.

---

#### **Constraint 5: No Built-In Concurrency Primitives**

**Given:**
- Claude Code orchestrator is markdown-based (not a programming language)
- No native `async`/`await`, threads, or process pools
- Task tool spawns agents sequentially by default

**Limitation:**
- Can't use `asyncio.gather()` or `Promise.all()` in orchestrator
- Parallel execution requires external coordination (message queue)

**Design Decision:**
> Implement **task queue pattern**: orchestrator enqueues N tasks, agents process in parallel, orchestrator polls for completion.

---

### 2.3 Operational Constraints

#### **Constraint 6: Single Developer, Low Ops Overhead**

**Requirements:**
- Must work on local MacBook (no cloud dependencies for MVP)
- Setup time <30 minutes
- Zero external services for MVP (Redis optional for production)
- Self-contained (no Kubernetes, Docker Compose, etc.)

**Design Decision:**
> Start with `asyncio.Queue` (in-memory), provide upgrade path to Redis for distributed execution.

---

#### **Constraint 7: INTJ/5w4 Alignment**

**Preferences:**
- Simplicity over features (minimal viable solution)
- Reversibility (easy to roll back)
- Evidence-driven (measure before optimizing)
- Composability (small, reusable pieces)
- Aesthetics (clean abstractions, elegant patterns)

**Design Decision:**
> Prioritize **phased implementation** (MVP → Production → Advanced) with gates at each phase.

---

## 3. Inter-Agent Communication: Problem Analysis

### 3.1 Communication Patterns (Taxonomy)

Given the constraints, what communication patterns are possible?

#### **Pattern 1: Orchestrator-Mediated (Hub-and-Spoke)**

**Current Default:**
```
Orchestrator → Agent A → Orchestrator → Agent B → Orchestrator
```

**Characteristics:**
- ✅ Simple, built-in (Task tool)
- ✅ Orchestrator has full visibility
- ❌ Sequential (no parallelism)
- ❌ Orchestrator becomes bottleneck

**Use Case:**
- Linear workflows (A must complete before B starts)
- Orchestrator needs to inspect/modify results between steps

---

#### **Pattern 2: Shared State (Blackboard)**

**Proposed:**
```
Orchestrator → Enqueue tasks → Queue
                                 ↓
Agent A → Read queue → Process → Write results → Shared State
Agent B → Read queue → Process → Write results → Shared State
Agent C → Read queue → Process → Write results → Shared State
                                 ↓
Orchestrator ← Poll for completion ← Shared State
```

**Characteristics:**
- ✅ Parallel execution (agents run simultaneously)
- ✅ Agents communicate via shared state (read/write)
- ✅ Orchestrator polls for completion (barrier)
- ⚠️ Requires external state store (Redis or asyncio.Queue)
- ❌ No direct agent-to-agent messaging

**Use Case:**
- Parallel fan-out (N agents doing same task with different inputs)
- Orchestrator needs to wait for all agents before proceeding (barrier)

---

#### **Pattern 3: Message Passing (Peer-to-Peer via Queue)**

**Proposed:**
```
Agent A → Publishes message to channel "agent_b_inbox"
                                 ↓
                            Message Queue
                                 ↓
Agent B → Polls "agent_b_inbox" → Receives message → Processes → Responds
```

**Characteristics:**
- ✅ Asynchronous communication (no blocking)
- ✅ Agents can send feedback to each other
- ⚠️ Requires polling (agents check inbox via MCP tool)
- ❌ Not truly peer-to-peer (still mediated by queue)
- ❌ Orchestrator must spawn all agents (agents can't spawn peers)

**Use Case:**
- Agent A finds issue in Agent B's output → sends revision request
- Agent B re-processes → publishes updated result
- skeptic-reviewer → ideation-scout feedback loop

---

#### **Pattern 4: Event-Driven (Pub/Sub)**

**Proposed:**
```
Agent A → Publishes event "DISCOVERY_COMPLETE" to channel "discovery"
                                 ↓
                         Pub/Sub System (Redis)
                                 ↓
Agent B → Subscribed to "discovery" → Receives event → Triggers action
Agent C → Subscribed to "discovery" → Receives event → Triggers action
```

**Characteristics:**
- ✅ Many-to-many communication
- ✅ Decoupled (publishers don't know subscribers)
- ⚠️ Requires Redis pub/sub (more complex than simple queue)
- ❌ Agents must poll subscriptions (no push notifications in MCP)
- ❌ Orchestrator still needs to spawn all agents

**Use Case:**
- Agent A completes → multiple agents react (validation, logging, aggregation)
- Event-driven workflows (not strictly sequential)

---

### 3.2 Recommended Communication Strategy

Given constraints, use **hybrid approach**:

#### **Primary: Shared State (Blackboard) Pattern**

**For parallel execution:**
```yaml
# Orchestrator enqueues tasks
for branch in [B1, B2, ..., B12]:
  enqueue_task(agent="ideation-scout", branch_id=branch, inputs={...})

# Agents process independently
Agent(ideation-scout, B1) → Reads task from queue → Processes → Writes result
Agent(ideation-scout, B2) → Reads task from queue → Processes → Writes result
...

# Orchestrator waits for all
wait_for_results(branch_ids=[B1, B2, ..., B12], timeout=300)
```

**Implementation:**
- Use MCP server with asyncio.Queue (MVP) or Redis (production)
- Tools: `enqueue_task`, `get_result`, `wait_for_results`, `queue_status`

---

#### **Secondary: Message Passing for Feedback Loops**

**For inter-agent communication:**
```yaml
# skeptic-reviewer finds issue in B3
skeptic-reviewer → send_message(
  to_agent="ideation-scout",
  branch_id="B3",
  message={issue: "Missing risk analysis", action: "REVISE"}
)

# ideation-scout checks inbox
ideation-scout(B3) → check_messages(agent="ideation-scout", branch_id="B3")
                  → Receives revision request
                  → Re-runs analysis
                  → Publishes updated result
```

**Implementation:**
- Use MCP tool: `send_message(to, message)`, `check_messages(agent_id)`
- Each agent checks inbox at start of execution
- Optional: orchestrator can route messages (agent A → orchestrator → agent B)

---

### 3.3 Is Redis/Message Queue Still Relevant?

**Short Answer: YES, but with caveats**

#### **Scenario 1: Parallel Execution Only**

**Need:** Run N agents in parallel, wait for all to complete

**Solution:** asyncio.Queue (in-memory) is sufficient
- ✅ Zero external dependencies
- ✅ Fast (in-memory)
- ✅ Simple (Python stdlib)
- ❌ Not distributed (single machine only)
- ❌ Lost on crash (no persistence)

**Verdict:** Start here (MVP)

---

#### **Scenario 2: Inter-Agent Communication**

**Need:** Agent A sends feedback to Agent B

**Solution:** Redis (persistent message queue)
- ✅ Persistent (survives crashes)
- ✅ Multi-machine (distributed)
- ✅ Pub/sub support (event-driven)
- ❌ External dependency (requires Redis server)
- ❌ More complex (setup, monitoring)

**Verdict:** Use for production or when N>50 agents

---

#### **Scenario 3: Orchestrator Constraints**

**Given:** Only orchestrator can spawn agents (subagents can't spawn peers)

**Impact on Message Queue:**
- Message queue is NOT for agent invocation (that's Task tool)
- Message queue IS for task distribution and data sharing
- Orchestrator still controls agent lifecycle (spawn, monitor, kill)

**Architecture:**
```
Orchestrator (Main Thread)
  ├─> Spawns Agent A (via Task tool)
  ├─> Spawns Agent B (via Task tool)
  └─> Spawns Agent C (via Task tool)
       ↓
  [All agents share access to Message Queue via MCP tool]
       ↓
Agent A → Writes to queue → Agent B reads (asynchronous communication)
```

**Key Insight:**
> Message queue is for **data/message passing**, not **agent invocation**. Orchestrator retains control of agent lifecycle.

**Verdict:** Redis/queue is STILL relevant for communication, just not for spawning agents.

---

## 4. Reusable Agent Library: Design Problem

### 4.1 Current Agent Specialization

**Existing agents are domain-specific:**

```markdown
# saas/ideation-scout.md
"Mine GitHub for monetizable SaaS opportunities using ggrep..."

# trading/regime-detector.md
"Detect market regime (IV, volatility, trend) for options trading..."
```

**Problem:**
- High coupling to domain (can't reuse ideation-scout for trading)
- Duplication across domains (similar patterns, different contexts)
- Hard to maintain (12 separate agent files)

### 4.2 Reusability Goals

**Goal:** Create agents that work across domains via parametrization

**Example:**
```markdown
# core/generic-researcher.md
---
name: generic-researcher
description: Research a topic using specified tools and return structured findings
---

When invoked, expect:
- research_topic: <what to research>
- tools: <list of tools to use: ggrep, web search, etc.>
- output_format: <desired structure: bullet points, table, etc.>
- domain_context: <optional: domain-specific constraints>

Method:
1. Use specified tools to gather information
2. Synthesize findings
3. Return results in specified format
```

**Usage:**
```yaml
# SaaS workflow
- agent: core/generic-researcher
  inputs:
    research_topic: "GitHub repos with monetization potential"
    tools: ["ggrep"]
    domain_context: "Focus on developer tools, B2B SaaS"

# Trading workflow
- agent: core/generic-researcher
  inputs:
    research_topic: "Current market regime for NIFTY"
    tools: ["market_data_api"]
    domain_context: "Options trading, IV analysis"
```

### 4.3 Agent Library Structure (Proposed)

#### **Tier 1: Core Generic Agents (Domain-Agnostic)**

```
.claude/agents/core/
├── generic-researcher.md       # Research + synthesis
├── generic-analyzer.md          # Data analysis + insights
├── generic-validator.md         # Quality checks + validation
├── generic-planner.md           # Plan generation + breakdown
├── decision-aggregator.md       # Score + rank options (existing)
├── self-approver.md             # Decision gate (existing)
└── skeptic-reviewer.md          # Critical review (existing)
```

**Characteristics:**
- Parametrized via inputs (not hardcoded domain knowledge)
- Tool-agnostic (use tools passed as inputs)
- Output structured data (JSON, tables, bullet points)
- No domain-specific terminology

---

#### **Tier 2: Domain Adapters (Thin Wrappers)**

```
.claude/agents/saas/
├── ideation-scout.md            # Wraps: generic-researcher
├── market-mapper.md             # Wraps: generic-analyzer
└── feasibility-engineer.md      # Wraps: generic-planner

.claude/agents/trading/
├── regime-detector.md           # Wraps: generic-analyzer
├── strategy-screener.md         # Wraps: generic-planner
└── backtest-sanity.md           # Wraps: generic-validator
```

**Characteristics:**
- Thin layer that calls generic agent with domain-specific inputs
- Provides domain vocabulary (TAM, IV, Greeks, etc.)
- Maps domain concepts to generic operations

**Example:**
```markdown
# saas/ideation-scout.md
---
name: ideation-scout
description: SaaS ideation via GitHub research
---

You are a SaaS ideation specialist. Your task is to delegate research to the generic-researcher agent.

When invoked with branch_id and problem_statement:
1. Call generic-researcher with:
   - research_topic: "GitHub repositories matching: ${problem_statement}"
   - tools: ["mcp__ggrep__searchGitHub"]
   - output_format: { ID, Idea, WhyNow, RepoSignals, MonetizationAngle, RiskTier, Links }
   - domain_context: "SaaS, B2B, developer tools. Focus on: stars, forks, issues, README quality."
2. Return results in exact SaaS format
```

**Benefit:**
- Core logic in generic-researcher (reusable)
- Domain-specific prompts in thin wrapper (maintainable)
- Can create new domain adapters without duplicating logic

---

#### **Tier 3: Workflow Orchestrators (Meta-Agents)**

```
.claude/agents/orchestration/
├── workflow-runner.md           # Execute YAML workflows
├── parallel-coordinator.md      # Fan-out/barrier pattern
└── feedback-loop-manager.md     # Inter-agent communication
```

**Characteristics:**
- Manage multi-agent workflows
- Handle task distribution and barriers
- Route messages between agents

---

### 4.4 Agent Communication Capabilities Matrix

| Agent Type | Can Spawn Agents? | Can Use Queue? | Can Send Messages? | Can Receive Messages? |
|------------|-------------------|----------------|--------------------|-----------------------|
| **Main Thread (Orchestrator)** | ✅ Yes (Task tool) | ✅ Yes (MCP) | ✅ Yes (MCP) | ✅ Yes (MCP) |
| **Tier 1: Core Generic** | ❌ No | ✅ Yes (MCP) | ✅ Yes (MCP) | ✅ Yes (MCP) |
| **Tier 2: Domain Adapters** | ❌ No | ✅ Yes (MCP) | ✅ Yes (MCP) | ✅ Yes (MCP) |
| **Tier 3: Orchestrators** | ❌ No* | ✅ Yes (MCP) | ✅ Yes (MCP) | ✅ Yes (MCP) |

*Note: Tier 3 orchestrators are still subagents, so they can't use Task tool. They coordinate via queue/messages, but actual agent spawning is done by main thread.

---

## 5. YAML Workflow System: Requirements

### 5.1 Workflow Definition Schema

**Required Elements:**

```yaml
# Minimal viable schema
name: string                    # Workflow identifier
version: string                 # Schema version (for compatibility)
description: string             # Human-readable description
domain: SaaS | Trading | Other  # Domain classification

inputs:                         # Workflow inputs
  - name: string
    type: string | integer | list | dict
    required: boolean
    default: any

stages:                         # Workflow stages
  - name: string                # Stage identifier
    type: parallel_fan_out | aggregate | gate | sequential
    agent: string               # Agent file path (e.g., "core/generic-researcher")
    depends_on: string          # Previous stage name (optional)
    branch_count: integer       # For parallel_fan_out
    branch_source: string       # For dynamic branching
    input_mapping: list         # Map workflow state to agent inputs
    output_mapping: list        # Map agent outputs to workflow state
    timeout: integer            # Seconds (optional)
    failure_strategy: fail_fast | log_and_continue | retry
    retry_policy:               # Optional
      max_attempts: integer
      backoff: linear | exponential

outputs:                        # Workflow outputs
  - name: string
    source: string              # JSONPath to workflow state
```

### 5.2 Stage Types (Primitives)

#### **Type 1: parallel_fan_out**

**Purpose:** Spawn N agents in parallel with same logic, different inputs

**Example:**
```yaml
- name: Discover
  type: parallel_fan_out
  agent: saas/ideation-scout
  branch_count: 12
  input_mapping:
    - from: "inputs.problem_statement"
      to: "problem_statement"
    - from: "stage.branch_id"  # Auto-generated: B1, B2, ..., B12
      to: "branch_id"
```

**Execution:**
1. Orchestrator enqueues 12 tasks to queue
2. Orchestrator spawns 12 agents (via Task tool, each reads from queue)
3. Agents process in parallel
4. Orchestrator waits for all to complete (barrier)

---

#### **Type 2: aggregate**

**Purpose:** Collect results from previous stage, synthesize

**Example:**
```yaml
- name: Aggregate_Discover
  type: aggregate
  agent: core/decision-aggregator
  depends_on: Discover
  input_mapping:
    - from: "Discover.*.output"  # All outputs from Discover stage
      to: "branch_outputs"
```

**Execution:**
1. Orchestrator waits for Discover stage to complete
2. Orchestrator collects all outputs (B1...B12)
3. Orchestrator spawns decision-aggregator with collected outputs
4. Aggregator returns summary

---

#### **Type 3: gate**

**Purpose:** Decision point (approve/reject/modify workflow)

**Example:**
```yaml
- name: Gate_Discover
  type: gate
  agent: core/self-approver
  depends_on: Aggregate_Discover
  input_mapping:
    - from: "Aggregate_Discover.output"
      to: "decision_brief"
  success_condition: "output.status == 'APPROVED'"
  on_failure:
    action: halt
    message: "Self-approver rejected at Discover stage"
```

**Execution:**
1. Orchestrator spawns self-approver with aggregated results
2. Self-approver returns decision (APPROVED | CHANGES_REQUIRED | REJECTED)
3. Orchestrator evaluates success_condition
4. If true: proceed to next stage
5. If false: execute on_failure action (halt, retry, backtrack)

---

#### **Type 4: sequential**

**Purpose:** Single agent execution (for clarity, not parallelism)

**Example:**
```yaml
- name: Generate_Report
  type: sequential
  agent: core/report-generator
  depends_on: Final_Gate
  input_mapping:
    - from: "workflow.state"
      to: "full_context"
```

---

### 5.3 Input/Output Mapping (Expression Language)

**Problem:** How to reference nested workflow state in YAML?

**Options:**

#### **Option A: JSONPath (Standard)**

```yaml
input_mapping:
  - from: "$.stages.Discover.branches[*].output"  # JSONPath syntax
    to: "branch_outputs"
```

**Pros:** Standard, widely supported, powerful
**Cons:** Complex syntax, requires parser library

---

#### **Option B: Dot Notation (Simple)**

```yaml
input_mapping:
  - from: "Discover.*.output"  # Simplified notation
    to: "branch_outputs"
```

**Pros:** Simple, readable, easy to parse
**Cons:** Limited expressiveness (no complex queries)

**Recommendation:** Start with Option B, add Option A if needed

---

#### **Option C: Explicit (No Expression Parsing)**

```yaml
input_mapping:
  source_stage: "Discover"
  source_field: "outputs"
  target_field: "branch_outputs"
  transform: "collect_all"  # collect_all, merge, filter
```

**Pros:** No parsing needed, explicit, debuggable
**Cons:** Verbose, less flexible

---

### 5.4 Workflow Execution Engine (Pseudocode)

```python
class WorkflowEngine:
    def __init__(self, workflow_yaml_path):
        self.workflow = load_yaml(workflow_yaml_path)
        self.state = {
            "inputs": {},
            "stages": {},
            "outputs": {}
        }

    async def execute(self, inputs):
        # Initialize workflow state
        self.state["inputs"] = inputs

        # Execute stages in order
        for stage in self.workflow.stages:
            # Check dependencies
            if stage.depends_on:
                await self.wait_for_stage(stage.depends_on)

            # Execute stage based on type
            if stage.type == "parallel_fan_out":
                result = await self.execute_parallel(stage)
            elif stage.type == "aggregate":
                result = await self.execute_aggregate(stage)
            elif stage.type == "gate":
                result = await self.execute_gate(stage)
            elif stage.type == "sequential":
                result = await self.execute_sequential(stage)

            # Store result in state
            self.state["stages"][stage.name] = result

            # Check if gate failed
            if stage.type == "gate" and not result.approved:
                self.handle_gate_failure(stage)
                break

        # Extract outputs
        return self.extract_outputs()

    async def execute_parallel(self, stage):
        # Enqueue N tasks
        for i in range(stage.branch_count):
            branch_id = f"B{i+1}"
            inputs = self.map_inputs(stage.input_mapping, {"branch_id": branch_id})
            await self.queue.enqueue_task(
                agent=stage.agent,
                branch_id=branch_id,
                inputs=inputs
            )

        # Spawn N agents (via Task tool - this is done by orchestrator)
        # Note: Task tool calls are synchronous, so we need to spawn in parallel
        # This is where the queue pattern helps

        # Wait for all to complete
        branch_ids = [f"B{i+1}" for i in range(stage.branch_count)]
        results = await self.queue.wait_for_results(branch_ids, timeout=stage.timeout)

        return results
```

---

## 6. Design Decisions & Rationale

### Decision 1: asyncio.Queue (MVP) → Redis (Production)

**Rationale:**
- asyncio.Queue has zero dependencies, works immediately
- Proves the pattern without external services
- Redis provides persistence and distribution for production scale

**Migration Path:**
```python
# MCP server interface stays the same:
@mcp.tool()
async def enqueue_task(agent, branch_id, inputs): ...

# Backend swaps:
# MVP: uses asyncio.Queue
# Production: uses Redis
```

**Gate:** Move to Redis only if N>50 or multi-machine needed

---

### Decision 2: Hybrid Communication (Shared State + Message Passing)

**Rationale:**
- Shared State (queue) for parallel execution (primary use case)
- Message Passing for feedback loops (secondary, optional)
- Both use same MCP server (unified interface)

**Priority:**
1. Implement Shared State first (enables parallelism)
2. Add Message Passing later (enables feedback loops)

---

### Decision 3: Three-Tier Agent Library

**Rationale:**
- Tier 1 (Core Generic): Maximum reusability, zero duplication
- Tier 2 (Domain Adapters): Domain-specific vocabulary, thin wrappers
- Tier 3 (Orchestrators): Workflow management, meta-agents

**Benefit:**
- New domains only need Tier 2 adapters (Tier 1 is reused)
- Reduces maintenance burden (12 agents → 7 core + 5 adapters per domain)

---

### Decision 4: Dot Notation for Input Mapping (Simple Expression Language)

**Rationale:**
- JSONPath is overkill for MVP (complex to parse)
- Explicit mapping is too verbose
- Dot notation strikes balance (readable, simple to parse)

**Syntax:**
```
"Discover.*.output"      → All outputs from Discover stage
"Discover.B3.output"     → Single branch output
"inputs.problem_statement" → Workflow input
"stage.branch_id"        → Current stage metadata
```

---

### Decision 5: Orchestrator Retains Agent Lifecycle Control

**Rationale:**
- Claude Code architecture: only main thread can spawn agents
- Message queue is for data, not invocation
- Clear separation of concerns: orchestrator = control plane, queue = data plane

**Implication:**
- Subagents can't spawn peers (they communicate via queue)
- Orchestrator must spawn all agents upfront (or on-demand based on queue state)

---

## 7. Implementation Phases

### Phase 0: Validation (2 hours)

**Goal:** Prove YAML pattern viability before building

**Tasks:**
1. Create simple YAML workflow (3 stages)
2. Manually execute (read YAML, invoke agents by hand)
3. Measure token cost (YAML vs markdown orchestrator)
4. Identify what can't be expressed in YAML

**Gate:**
- ✅ YAML captures workflow clearly
- ✅ Token savings >20%
- ❌ If major gaps found: revisit approach

---

### Phase 1: Message Queue MVP (4 hours)

**Goal:** Enable parallel agent execution

**Deliverables:**
- `.claude/mcp/simple-queue.py` (asyncio.Queue-based)
- MCP tools: `enqueue_task`, `get_result`, `wait_for_results`, `queue_status`
- Test with 3-branch workflow (manual YAML execution)

**Success Criteria:**
- ✅ 3 agents run in parallel (not sequential)
- ✅ Latency <40s for N=3 (vs ~60s sequential)
- ✅ Zero external dependencies

**Gate:** Only proceed if 2x+ speedup achieved

---

### Phase 2: YAML Schema + Hardcoded Executor (8 hours)

**Goal:** Prove YAML workflow pattern

**Deliverables:**
- YAML schema definition (Pydantic models)
- Hardcoded workflow executor in `explore.md` (supports 3 stage types)
- 2 example workflows: `saas_simple.yaml`, `trading_simple.yaml`

**Success Criteria:**
- ✅ Can define workflows in YAML
- ✅ Executor runs 3-stage workflow correctly
- ✅ Adding new stage = YAML edit, not code edit

**Gate:** Only proceed if YAML is significantly clearer than markdown

---

### Phase 3: Generic Workflow Engine (16 hours)

**Goal:** Production-grade engine with full features

**Deliverables:**
- `.claude/agents/orchestration/workflow-runner.md` (generic executor)
- Expression parser (dot notation)
- Error handling, retry logic
- State checkpointing (resume from failure)
- 5+ example workflows (different domains)

**Success Criteria:**
- ✅ Supports all 4 stage types
- ✅ Expression mapping works
- ✅ Can resume from checkpoint

**Gate:** Only proceed if generic engine is stable

---

### Phase 4: Three-Tier Agent Library (12 hours)

**Goal:** Reusable agent library

**Deliverables:**
- 7 core generic agents (Tier 1)
- Refactor existing 12 agents as Tier 2 adapters
- Documentation for creating new domain adapters

**Success Criteria:**
- ✅ Core agents work across domains
- ✅ New domain adapter <1 hour to create
- ✅ Zero duplication in core logic

**Gate:** Only proceed if reusability is proven (2+ domains)

---

### Phase 5: Inter-Agent Communication (8 hours)

**Goal:** Enable feedback loops

**Deliverables:**
- MCP tools: `send_message`, `check_messages`
- Example: skeptic-reviewer → ideation-scout feedback loop
- Workflow example with revision stages

**Success Criteria:**
- ✅ Agent A can send message to Agent B
- ✅ Agent B processes and responds
- ✅ Orchestrator can monitor message flow

---

### Phase 6: Redis Upgrade (4 hours)

**Goal:** Production scalability

**Deliverables:**
- `.claude/mcp/redis-queue.py` (drop-in replacement)
- Same MCP tool interface (no workflow changes)
- Persistence and multi-machine support

**Trigger:** N>50 or multi-machine deployment needed

---

## 8. Open Questions & Research Needed

### Q1: Expression Language Complexity

**Question:** Is dot notation sufficient, or do we need full JSONPath?

**Research Needed:**
- Catalog all real-world mapping patterns from existing workflows
- Identify edge cases (nested arrays, conditional mapping, transforms)

**Decision Point:** Phase 2 (hardcoded executor will reveal gaps)

---

### Q2: Workflow Composition

**Question:** Can workflows call other workflows? (Sub-workflows)

**Example:**
```yaml
- name: Deep_Market_Analysis
  type: sub_workflow
  workflow: market_research.yaml
  input_mapping: ...
```

**Research Needed:**
- Does this add significant value?
- How to handle nested context (sub-workflow state)?

**Decision Point:** Phase 3 (if users request it)

---

### Q3: Dynamic Branching

**Question:** Can branch count be determined at runtime?

**Example:**
```yaml
- name: Validate
  type: parallel_fan_out
  branch_source: "Gate_Discover.output.approved_branches"  # Dynamic list
  agent: saas/market-mapper
```

**Research Needed:**
- How common is this pattern?
- Adds complexity to executor (dynamic agent spawning)

**Decision Point:** Phase 2 (hardcoded first, generalize later)

---

### Q4: Conditional Stages

**Question:** Can stages be conditionally executed?

**Example:**
```yaml
- name: Deep_Analysis
  type: sequential
  agent: deep-analyzer
  condition: "Aggregate.output.uncertainty > 0.7"  # Only run if uncertain
```

**Research Needed:**
- How to parse condition expressions?
- Adds significant complexity (expression evaluator)

**Decision Point:** Phase 3 (advanced feature, not MVP)

---

### Q5: Loop/Iteration

**Question:** Can stages loop until condition met?

**Example:**
```yaml
- name: Refine_Until_Approved
  type: loop
  max_iterations: 3
  agent: idea-refiner
  exit_condition: "self-approver.status == 'APPROVED'"
```

**Research Needed:**
- How common is iterative refinement?
- Risk of infinite loops (need max_iterations)

**Decision Point:** Phase 3 (advanced feature)

---

### Q6: Workflow Versioning

**Question:** How to handle breaking changes in YAML schema?

**Strategy:**
```yaml
version: "1.0"  # Schema version
# Engine validates and migrates if needed
```

**Research Needed:**
- How to maintain backward compatibility?
- When to break compatibility vs. evolve schema?

**Decision Point:** Phase 3 (when schema stabilizes)

---

## 9. Success Metrics & Observability

### Performance Metrics

| Metric | Baseline | Target | Measurement |
|--------|----------|--------|-------------|
| Latency (N=12 parallel) | 120s | <40s | Time from start to barrier complete |
| Token Cost (orchestration) | 8K tokens | <2K tokens | Workflow def + engine overhead |
| Context Usage (per stage) | 30-40% | <20% | /cost command output |
| Agent Spawn Time | N/A | <2s per agent | Task tool invocation time |
| Queue Throughput | N/A | >10 tasks/sec | enqueue → process latency |

### Observability Requirements

**Queue Status:**
```json
{
  "stage": "Discover",
  "pending_tasks": 12,
  "running_tasks": 8,
  "completed_tasks": 0,
  "failed_tasks": 0,
  "oldest_pending": "2.3s"
}
```

**Agent Status:**
```json
{
  "agent": "ideation-scout",
  "branch_id": "B3",
  "status": "running",
  "started_at": "2025-10-20T10:15:30Z",
  "elapsed": "15.3s",
  "last_tool_call": "mcp__ggrep__searchGitHub"
}
```

**Workflow Progress:**
```json
{
  "workflow": "saas_workflow.yaml",
  "current_stage": "Aggregate_Discover",
  "stages_complete": 2,
  "stages_total": 8,
  "elapsed": "45.2s",
  "estimated_remaining": "120s"
}
```

### Error Monitoring

**Required:**
- Failed agent count + failure reasons
- Retry attempts + success rate
- Timeout occurrences
- Queue overflow (if bounded queue)

---

## 10. Risk Analysis & Mitigation

### Risk 1: Implementation Complexity Underestimated

**Probability:** High
**Impact:** High (timeline, scope creep)

**Mitigation:**
- Phased approach with gates at each phase
- MVP scope strictly limited (3 stage types, no expression parsing)
- Time-box each phase (don't over-engineer)

---

### Risk 2: YAML Pattern Doesn't Provide Value

**Probability:** Medium
**Impact:** High (wasted effort)

**Mitigation:**
- Phase 0 validation before building
- Measure token savings empirically
- Keep markdown orchestrator as fallback

---

### Risk 3: Queue Becomes Bottleneck

**Probability:** Low (N=12), High (N=100)
**Impact:** Medium (performance degradation)

**Mitigation:**
- Start with asyncio.Queue (fast for N<50)
- Monitor queue latency
- Upgrade to Redis only if bottleneck confirmed

---

### Risk 4: Inter-Agent Communication Too Complex

**Probability:** Medium
**Impact:** Medium (delayed feature)

**Mitigation:**
- Implement in Phase 5 (after core workflow works)
- Start with simple message passing (no pub/sub)
- Make it optional (workflows work without it)

---

### Risk 5: Agent Library Reusability Overestimated

**Probability:** Medium
**Impact:** Medium (duplicate agents per domain)

**Mitigation:**
- Test reusability with 2+ domains before declaring success
- Accept domain-specific agents if generic version is too complex
- Prefer pragmatism over purity

---

## 11. Dependencies & Prerequisites

### Technical Dependencies

**Required:**
- Python 3.10+ (for asyncio, type hints)
- Claude Code v1.0.88+ (for MCP, Task tool)
- PyYAML (for YAML parsing)
- Pydantic (for schema validation)

**Optional (Production):**
- Redis 7.0+ (for distributed queue)
- redis-py (Python Redis client)

### Knowledge Dependencies

**Required:**
- Claude Code agent architecture (file-based, Task tool)
- MCP server development (stdio transport)
- YAML syntax and parsing
- asyncio programming (for queue implementation)

**Nice to Have:**
- Redis pub/sub patterns
- Expression language design (for input mapping)
- Workflow engine patterns (Airflow, Temporal)

---

## 12. Alignment with INTJ/5w4 Preferences

### Ni (Dominant): Pattern Recognition

✅ **Aligned:**
- YAML workflows = abstracted pattern of multi-agent orchestration
- Three-tier agent library = meta-pattern (generic → specialized)
- Phased approach = evolutionary refinement of initial vision

### Te (Auxiliary): Systematization

✅ **Aligned:**
- Formal schema (YAML, Pydantic models)
- Structured phases with clear gates
- Metrics-driven decisions (token cost, latency)

### Fi (Tertiary): Values Alignment

✅ **Aligned:**
- Simplicity over features (MVP-first)
- Reversibility (keep markdown orchestrator as fallback)
- Evidence-driven (measure before optimizing)

### Se (Inferior): Practical Execution

⚠️ **Watch Out For:**
- Over-planning (build vs. theorize)
- Perfectionism (don't over-engineer Phase 1)
- Scope creep (stick to phased approach)

**Mitigation:**
- Time-box each phase
- Ship MVP quickly, iterate
- Use gates to force decision points

---

## 13. Next Steps (Immediate Actions)

### Week 1: Phase 0 Validation

**Monday:**
1. Create `saas_simple.yaml` (3-stage workflow)
2. Calculate token cost (YAML + minimal engine vs. current explore.md)
3. Manually execute workflow (simulate engine)

**Gate Decision:**
- If token savings <20%: Revisit approach
- If YAML doesn't capture workflow clearly: Stick with markdown
- If validation passes: Proceed to Phase 1

---

### Week 2-3: Phase 1 MVP

**Deliverables:**
- `simple-queue.py` MCP server
- Test with 3-branch parallel workflow
- Measure latency improvement

**Gate Decision:**
- If speedup <2x: Investigate bottleneck
- If queue pattern is too complex: Simplify
- If validation passes: Proceed to Phase 2

---

### Week 4-5: Phase 2 Hardcoded Executor

**Deliverables:**
- YAML schema (Pydantic)
- Hardcoded executor in explore.md
- 2 example workflows

**Gate Decision:**
- If YAML adds complexity without benefit: Revert
- If executor is stable and useful: Proceed to Phase 3
- If gaps identified: Revisit schema

---

## 14. Appendix: Glossary

**Agent:** Pre-defined AI assistant with specific role (file: `.claude/agents/*.md`)

**Orchestrator:** Main thread that spawns and coordinates agents (current: `explore.md`)

**Subagent:** Agent spawned by orchestrator (via Task tool)

**Task Queue:** Message queue for distributing work to agents (Redis or asyncio.Queue)

**Barrier:** Synchronization point (wait for all parallel agents to complete)

**Fan-out:** Spawn N agents in parallel

**Stage:** Unit of work in workflow (parallel_fan_out, aggregate, gate, sequential)

**Input Mapping:** How to map workflow state to agent inputs

**Output Mapping:** How to map agent outputs back to workflow state

**Gate:** Decision point in workflow (approve/reject/modify flow)

**Tier 1 Agent:** Core generic agent (reusable across domains)

**Tier 2 Agent:** Domain adapter (thin wrapper around Tier 1)

**Tier 3 Agent:** Workflow orchestrator (meta-agent)

**MCP:** Model Context Protocol (Claude Code's tool integration system)

**Hub-and-Spoke:** Orchestrator ↔ agents (current communication pattern)

**Shared State (Blackboard):** Agents read/write to common state store

**Message Passing:** Agents send asynchronous messages to each other

**Pub/Sub:** Event-driven pattern (publishers/subscribers)

---

## 15. Document Metadata

**Version:** 1.0
**Last Updated:** 2025-10-20
**Authors:** Solo developer (INTJ/5w4), Claude (analysis assistant)
**Status:** Design Phase
**Next Review:** After Phase 0 validation

**Change Log:**
- 2025-10-20: Initial draft (comprehensive problem statement)

**Related Documents:**
- `explore.md` (current orchestrator implementation)
- `.claude/agents/*` (existing agent definitions)
- `mcp.json` (MCP server configuration)
- `CLAUDE.md` (repository-level instructions)

---

**END OF PROBLEM STATEMENT**
