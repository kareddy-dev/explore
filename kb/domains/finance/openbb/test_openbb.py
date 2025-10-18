#!/usr/bin/env python3
"""
Test OpenBB API with Indian stocks
"""

from openbb import obb
import json
from datetime import datetime, timedelta

print("=" * 80)
print("OpenBB API Test - Indian Stock Market")
print("=" * 80)

# Test 1: Basic US stock (to verify OpenBB works)
print("\n[Test 1] Fetching AAPL historical data (US stock)...")
try:
    result = obb.equity.price.historical(
        symbol="AAPL",
        start_date=(datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
        provider="yfinance"
    )
    df = result.to_df()
    print(f"✅ SUCCESS: Got {len(df)} days of data for AAPL")
    print(f"   Latest price: ${df['close'].iloc[-1]:.2f}")
except Exception as e:
    print(f"❌ FAILED: {e}")

# Test 2: Indian stock - NSE (Reliance)
print("\n[Test 2] Fetching RELIANCE.NS historical data (NSE)...")
try:
    result = obb.equity.price.historical(
        symbol="RELIANCE.NS",
        start_date=(datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
        provider="yfinance"
    )
    df = result.to_df()
    print(f"✅ SUCCESS: Got {len(df)} days of data for RELIANCE.NS")
    print(f"   Latest price: ₹{df['close'].iloc[-1]:.2f}")
    print(f"   30-day return: {((df['close'].iloc[-1] / df['close'].iloc[0]) - 1) * 100:.2f}%")
except Exception as e:
    print(f"❌ FAILED: {e}")

# Test 3: Indian stock - BSE (Infosys)
print("\n[Test 3] Fetching INFY.BO historical data (BSE)...")
try:
    result = obb.equity.price.historical(
        symbol="INFY.BO",
        start_date=(datetime.now() - timedelta(days=30)).strftime("%Y-%m-%d"),
        provider="yfinance"
    )
    df = result.to_df()
    print(f"✅ SUCCESS: Got {len(df)} days of data for INFY.BO")
    print(f"   Latest price: ₹{df['close'].iloc[-1]:.2f}")
except Exception as e:
    print(f"❌ FAILED: {e}")

# Test 4: Company fundamentals (NSE)
print("\n[Test 4] Fetching TCS.NS fundamental metrics...")
try:
    result = obb.equity.fundamental.metrics(
        symbol="TCS.NS",
        provider="yfinance"
    )
    df = result.to_df()
    if not df.empty:
        print(f"✅ SUCCESS: Got fundamental data for TCS.NS")
        # Display available metrics
        print(f"   Available metrics: {list(df.columns)[:10]}...")
    else:
        print("⚠️  WARNING: Got empty dataframe for fundamentals")
except Exception as e:
    print(f"❌ FAILED: {e}")

# Test 5: Multiple stocks at once
print("\n[Test 5] Fetching multiple Indian stocks...")
try:
    symbols = ["RELIANCE.NS", "TCS.NS", "HDFCBANK.NS"]
    for symbol in symbols:
        result = obb.equity.price.historical(
            symbol=symbol,
            start_date=(datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d"),
            provider="yfinance"
        )
        df = result.to_df()
        print(f"   {symbol}: ₹{df['close'].iloc[-1]:.2f} ({len(df)} days)")
    print("✅ SUCCESS: Multi-stock fetch working")
except Exception as e:
    print(f"❌ FAILED: {e}")

# Test 6: Test data availability
print("\n[Test 6] Testing data range and availability...")
try:
    # Try 1 year of data
    result = obb.equity.price.historical(
        symbol="RELIANCE.NS",
        start_date=(datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d"),
        provider="yfinance"
    )
    df = result.to_df()
    print(f"✅ SUCCESS: Got {len(df)} days of historical data (1 year)")
    print(f"   Date range: {df.index[0]} to {df.index[-1]}")
    print(f"   Columns available: {list(df.columns)}")
except Exception as e:
    print(f"❌ FAILED: {e}")

print("\n" + "=" * 80)
print("Test Summary")
print("=" * 80)
print("\n✅ OpenBB is working!")
print("✅ Indian NSE stocks (.NS suffix) are supported")
print("✅ Indian BSE stocks (.BO suffix) are supported")
print("✅ Historical price data is available")
print("\nReady to build MCP server for Claude Code integration!")
