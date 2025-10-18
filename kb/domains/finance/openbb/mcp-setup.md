# OpenBB MCP Server Setup

**Domain:** Finance
**Created:** 2025-10-18
**Status:** Ready to implement

---

## 📊 Overview

This document explains how to integrate OpenBB with Claude Code using MCP (Model Context Protocol).

**What you get:**
- Natural language queries for stock data
- Automated financial analysis
- Direct OpenBB integration with Claude

---

## 🚀 Quick Setup

### Prerequisites
```bash
pip install openbb fastmcp
```

### Configuration
The complete MCP server implementation is available in this directory. See the main OpenBB documentation for details.

---

## 🧪 Testing Scripts

This directory includes test scripts to verify OpenBB functionality:

- **test_openbb.py** - Basic functionality tests for Indian stocks
- **test_openbb_advanced.py** - Advanced features testing

Run tests:
```bash
cd kb/domains/finance/openbb/
python test_openbb.py
python test_openbb_advanced.py
```

---

## 💡 Usage Examples

Once setup, you can:
```
"Analyze RELIANCE stock"
"Compare TCS and INFY fundamentals"
"Screen Nifty 50 for undervalued stocks"
```

---

## 🔗 References

- [OpenBB Capabilities](capabilities.md) - What data is available
- [Quick Reference](quick-reference.md) - Common queries
- [Test Results](test-results.md) - Verified functionality
- [Test Scripts](test_openbb.py) - Runnable tests

---

**Note:** Full MCP server implementation available upon request.
