# Finance Domain Index

**Domain:** Finance
**Last Updated:** 2025-01-18
**Topics:** OpenBB, Stocks, Strategies, Tools

---

## 📊 Domain Overview

This domain contains all financial analysis knowledge including:
- OpenBB Platform documentation and capabilities
- Individual stock research and analysis
- Trading and investing strategies
- Financial calculation tools and scripts

---

## 📚 Contents

### OpenBB Platform
**Path:** `openbb/`
**Status:** Active
**Documents:** 7

| Document | Description | Last Updated |
|----------|-------------|--------------|
| [capabilities.md](openbb/capabilities.md) | Complete OpenBB features and limitations | 2025-10-18 |
| [quick-reference.md](openbb/quick-reference.md) | Quick lookup tables | 2025-10-18 |
| [test-results.md](openbb/test-results.md) | Actual test data | 2025-10-18 |
| [mcp-setup.md](openbb/mcp-setup.md) | Claude Code integration | 2025-10-18 |
| [test_openbb.py](openbb/test_openbb.py) | Basic functionality tests | 2025-10-18 |
| [test_openbb_advanced.py](openbb/test_openbb_advanced.py) | Advanced features tests | 2025-10-18 |
| [test_nsepython.py](openbb/test_nsepython.py) | ✅ **VERIFIED** - nsepython NIFTY options test | 2025-01-18 |

**Quick Answers:**
- Can I get NSE stock prices? → ✅ YES, see capabilities.md
- Real-time data available? → ❌ NO, 15-min delay
- Indian stocks supported? → ✅ YES, NSE/BSE
- **NIFTY options with OI/Volume?** → ✅ YES, nsepython VERIFIED WORKING (see test_nsepython.py)

### Stock Analysis
**Path:** `stocks/`
**Status:** Active
**Documents:** 0

*No stock analyses yet. Use template: `../../templates/stock-analysis.md`*

**Naming Convention:** `[SYMBOL].md` (e.g., RELIANCE.md, TCS.md)

### Strategies
**Path:** `strategies/`
**Status:** Active
**Documents:** 1

| Document | Description | Last Updated |
|----------|-------------|--------------|
| [llm-analysis-prompts.md](strategies/llm-analysis-prompts.md) | Production-ready financial analysis prompts from 17+ GitHub projects (30+ patterns) | 2025-01-18 |

**Quick Answers:**
- How to prompt LLMs for stock analysis? → See llm-analysis-prompts.md Pattern 1.2
- Multi-agent financial analysis? → See Pattern 12.1 (Collaborative Swarm)
- Investment thesis format? → See Pattern 5.1 (Bull/Bear framework)
- Portfolio management prompts? → See Pattern 6.1

### Tools
**Path:** `tools/`
**Status:** Active
**Documents:** 2

| Document | Description | Last Updated |
|----------|-------------|--------------|
| [free-tools-ecosystem.md](tools/free-tools-ecosystem.md) | Free tools that complement OpenBB (yfinance, TA-Lib, Streamlit, Backtrader, etc.) | 2025-01-18 |
| [nifty-options-data-libraries.md](tools/nifty-options-data-libraries.md) | 5+ Python libraries for NIFTY options data with liquidity metrics (OI, Volume, Bid/Ask) | 2025-01-18 |

**Quick Answers:**
- What free tools work with OpenBB? → See free-tools-ecosystem.md
- Which technical analysis library? → TA-Lib (professional) or pandas_ta (easy)
- How to build dashboards? → Streamlit + Plotly
- Backtesting framework? → Backtrader
- **NIFTY options data with liquidity?** → See nifty-options-data-libraries.md (nsepython recommended)

---

## 🔍 Quick Reference

### Common Questions

**Q: How do I analyze an Indian stock?**
A: Use OpenBB with `.NS` suffix for NSE or `.BO` for BSE. See [openbb/capabilities.md](openbb/capabilities.md)

**Q: What financial metrics can I calculate?**
A: P/E, ROE, Sharpe ratio, VaR, and more. See [openbb/capabilities.md#metrics](openbb/capabilities.md)

**Q: Can I do technical analysis?**
A: Yes, 50+ indicators available. See [openbb/capabilities.md#technical](openbb/capabilities.md)

---

## 📈 Recently Updated

- 2025-01-18: **NIFTY options data libraries** - 5 libraries for options with liquidity metrics (OI, Volume, Bid/Ask)
- 2025-01-18: **LLM analysis prompts collection** - 30+ production-tested patterns from 17 GitHub projects
- 2025-01-18: Free tools ecosystem guide added (yfinance, TA-Lib, Streamlit, Backtrader, pandas_ta, Plotly, mplfinance)
- 2025-10-18: OpenBB documentation added (capabilities, quick-reference, test-results, mcp-setup)

---

## 🎯 Getting Started

1. **For stock analysis:**
   - Read [openbb/capabilities.md](openbb/capabilities.md) to understand what's possible
   - Use template at `../../templates/stock-analysis.md`
   - Save to `stocks/[SYMBOL].md`

2. **For API usage:**
   - See [openbb/mcp-setup.md](openbb/mcp-setup.md) for Claude Code integration
   - Check [openbb/quick-reference.md](openbb/quick-reference.md) for quick answers

3. **For using free tools:**
   - See [tools/free-tools-ecosystem.md](tools/free-tools-ecosystem.md) for comprehensive tool guide
   - Recommended: yfinance (data), TA-Lib (analysis), Streamlit (dashboards)
   - All tools are free and work with Indian stocks

4. **For creating custom tools:**
   - Save Python scripts to `tools/`
   - Document usage in script header

---

## 💡 Tips

- Use OpenBB for Indian stocks: Add `.NS` for NSE or `.BO` for BSE
- Historical data goes back 10+ years
- Real-time delayed by 15-20 minutes
- Ask Claude: "Analyze [SYMBOL] stock using OpenBB"

---

[← Back to Main Index](../../INDEX.md)
