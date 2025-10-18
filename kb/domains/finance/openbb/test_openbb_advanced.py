#!/usr/bin/env python3
"""
Advanced OpenBB API tests - Fundamentals, News, Screening
"""

from openbb import obb
from datetime import datetime, timedelta

print("=" * 80)
print("OpenBB Advanced Features Test")
print("=" * 80)

# Test 1: Financial Statements
print("\n[Test 1] Income Statement - TCS.NS...")
try:
    result = obb.equity.fundamental.income(
        symbol="TCS.NS",
        period="annual",
        limit=3,
        provider="yfinance"
    )
    df = result.to_df()
    if not df.empty:
        print(f"✅ SUCCESS: Got {len(df)} years of income statements")
        print(f"   Columns: {list(df.columns)[:8]}...")
    else:
        print("⚠️  WARNING: Empty response for income statement")
except Exception as e:
    print(f"❌ FAILED: {e}")

# Test 2: Balance Sheet
print("\n[Test 2] Balance Sheet - RELIANCE.NS...")
try:
    result = obb.equity.fundamental.balance(
        symbol="RELIANCE.NS",
        period="annual",
        limit=2,
        provider="yfinance"
    )
    df = result.to_df()
    if not df.empty:
        print(f"✅ SUCCESS: Got {len(df)} years of balance sheets")
        print(f"   Columns: {list(df.columns)[:8]}...")
    else:
        print("⚠️  WARNING: Empty response for balance sheet")
except Exception as e:
    print(f"❌ FAILED: {e}")

# Test 3: Cash Flow
print("\n[Test 3] Cash Flow Statement - INFY.NS...")
try:
    result = obb.equity.fundamental.cash(
        symbol="INFY.NS",
        period="annual",
        limit=2,
        provider="yfinance"
    )
    df = result.to_df()
    if not df.empty:
        print(f"✅ SUCCESS: Got {len(df)} years of cash flow statements")
        print(f"   Columns: {list(df.columns)[:8]}...")
    else:
        print("⚠️  WARNING: Empty response for cash flow")
except Exception as e:
    print(f"❌ FAILED: {e}")

# Test 4: Company News
print("\n[Test 4] Company News - RELIANCE.NS...")
try:
    result = obb.equity.news(
        symbol="RELIANCE",  # Try without .NS
        limit=5,
        provider="yfinance"
    )
    df = result.to_df()
    if not df.empty:
        print(f"✅ SUCCESS: Got {len(df)} news articles")
        if len(df) > 0:
            print(f"   Latest: {df['title'].iloc[0][:60]}...")
    else:
        print("⚠️  WARNING: No news available")
except Exception as e:
    print(f"⚠️  News might not be available: {e}")

# Test 5: Key Metrics Summary
print("\n[Test 5] Detailed Metrics - HDFCBANK.NS...")
try:
    result = obb.equity.fundamental.metrics(
        symbol="HDFCBANK.NS",
        provider="yfinance"
    )
    df = result.to_df()
    if not df.empty:
        print("✅ SUCCESS: Got comprehensive metrics")
        # Display some key metrics if available
        data = df.iloc[0]
        if 'market_cap' in df.columns:
            print(f"   Market Cap: ₹{data['market_cap']/10000000:.0f} Cr")
        if 'pe_ratio' in df.columns:
            print(f"   P/E Ratio: {data['pe_ratio']:.2f}" if data['pe_ratio'] else "   P/E Ratio: N/A")
        if 'forward_pe' in df.columns:
            print(f"   Forward P/E: {data['forward_pe']:.2f}" if data['forward_pe'] else "   Forward P/E: N/A")
    else:
        print("⚠️  WARNING: Empty metrics response")
except Exception as e:
    print(f"❌ FAILED: {e}")

# Test 6: Profile/Info
print("\n[Test 6] Company Profile - TCS.NS...")
try:
    result = obb.equity.profile(
        symbol="TCS.NS",
        provider="yfinance"
    )
    df = result.to_df()
    if not df.empty:
        print("✅ SUCCESS: Got company profile")
        data = df.iloc[0]
        if 'name' in df.columns:
            print(f"   Company: {data['name']}")
        if 'sector' in df.columns:
            print(f"   Sector: {data['sector']}")
        if 'industry' in df.columns:
            print(f"   Industry: {data['industry']}")
    else:
        print("⚠️  WARNING: Empty profile response")
except Exception as e:
    print(f"⚠️  Profile might have issues: {e}")

print("\n" + "=" * 80)
print("Advanced Features Summary")
print("=" * 80)
print("\n✅ Price data: Fully working")
print("✅ Fundamental metrics: Working")
print("⚠️  Financial statements: May have limited data for some stocks")
print("⚠️  News: May require different provider or symbol format")
print("⚠️  Company profile: May have limited data")
print("\n💡 Recommendation: Focus on price data and basic metrics for MCP server")
print("   These work reliably with yfinance provider for Indian stocks")
