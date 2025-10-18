# Finance Domain Index

**Domain:** Finance
**Last Updated:** 2025-10-18
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
**Documents:** 6

| Document | Description | Last Updated |
|----------|-------------|--------------|
| [capabilities.md](openbb/capabilities.md) | Complete OpenBB features and limitations | 2025-10-18 |
| [quick-reference.md](openbb/quick-reference.md) | Quick lookup tables | 2025-10-18 |
| [test-results.md](openbb/test-results.md) | Actual test data | 2025-10-18 |
| [mcp-setup.md](openbb/mcp-setup.md) | Claude Code integration | 2025-10-18 |
| [test_openbb.py](openbb/test_openbb.py) | Basic functionality tests | 2025-10-18 |
| [test_openbb_advanced.py](openbb/test_openbb_advanced.py) | Advanced features tests | 2025-10-18 |

**Quick Answers:**
- Can I get NSE stock prices? → ✅ YES, see capabilities.md
- Real-time data available? → ❌ NO, 15-min delay
- Indian stocks supported? → ✅ YES, NSE/BSE

### Stock Analysis
**Path:** `stocks/`
**Status:** Active
**Documents:** 0

*No stock analyses yet. Use template: `../../templates/stock-analysis.md`*

**Naming Convention:** `[SYMBOL].md` (e.g., RELIANCE.md, TCS.md)

### Strategies
**Path:** `strategies/`
**Status:** Active
**Documents:** 0

*No strategies documented yet.*

### Tools
**Path:** `tools/`
**Status:** Active
**Documents:** 0

*No tools created yet.*

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

3. **For creating tools:**
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
