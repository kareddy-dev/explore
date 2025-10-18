# NIFTY Options Data Libraries - Complete Guide

**Domain:** Finance
**Type:** Tool Collection
**Created:** 2025-01-18
**Last Updated:** 2025-01-18
**Purpose:** Libraries for fetching Indian options data with liquidity metrics
**Tags:** nifty, bank-nifty, options, option-chain, open-interest, liquidity, nse

---

## 📊 Overview

**What this is:**
A comprehensive guide to Python libraries that fetch NIFTY and Bank NIFTY options data directly from NSE, including critical liquidity metrics like Open Interest (OI), Volume, Bid/Ask spreads, and Implied Volatility (IV).

**Why these matter:**
- ✅ **Real NSE data** - Direct from National Stock Exchange
- ✅ **Free** - No paid APIs required
- ✅ **Liquidity metrics** - OI, Volume, Bid/Ask for trade execution
- ✅ **Live data** - Near real-time option chain updates
- ✅ **Multiple strikes** - Complete option chain for all strike prices
- ✅ **All expiries** - Weekly, monthly, and far-month contracts

**Critical for:**
- Options trading strategies
- Liquidity analysis (which strikes are tradeable)
- Max Pain calculations
- Put-Call Ratio (PCR) analysis
- Open Interest analysis
- Identifying institutional positions

---

## 🏆 Top Libraries Comparison

| Library | Author | Stars | Active | Liquidity Data | Best For |
|---------|--------|-------|--------|----------------|----------|
| **nsepython** | aeron7 | ⭐⭐⭐⭐ | ✅ Yes | OI, ΔOI, Volume, Bid/Ask, IV | Most comprehensive |
| **nselib** | RuchiTanmay | ⭐⭐⭐ | ✅ Yes | OI, ΔOI, Volume, IV | Clean API |
| **jugaad-data** | jugaad-py | ⭐⭐⭐⭐ | ✅ Yes | Full option chain | Historical + Live |
| **nsetools** | vsjha18 | ⭐⭐⭐ | ✅ Yes | OI, ΔOI, Volume | Derivatives focus |
| **nsedt** | pratik141 | ⭐⭐ | ✅ Yes | Option chain | Simple API |

---

## 1️⃣ nsepython - Most Comprehensive (Recommended)

**Repository:** https://github.com/aeron7/nsepython
**License:** GPL-3.0
**Status:** ✅ Actively maintained

### Features
- ✅ Live NIFTY/Bank NIFTY option chain
- ✅ **All liquidity metrics**: OI, Change in OI, Volume, Bid/Ask, IV
- ✅ Multiple expiry dates support
- ✅ Compact and full modes
- ✅ Pre-market and after-market data
- ✅ FII/DII data

### Installation
```bash
pip install nsepython
```

### Quick Start - Get NIFTY Option Chain with Liquidity
```python
from nsepython import *
import pandas as pd

# Get NIFTY option chain for current expiry
option_chain = nse_optionchain_scrapper("NIFTY")

# Display option chain with all liquidity data
print(option_chain)

# Access specific data
spot_price = option_chain['records']['underlyingValue']
expiry_dates = option_chain['records']['expiryDates']

print(f"NIFTY Spot: {spot_price}")
print(f"Available Expiries: {expiry_dates}")
```

### Get Option Chain with Liquidity Metrics
```python
# Get detailed option chain for specific expiry
expiry = "30-Jan-2025"  # Format: DD-MMM-YYYY

data = nse_optionchain_scrapper("NIFTY")

# Extract option chain data
option_data = data['records']['data']

# Create DataFrame with liquidity metrics
rows = []
for item in option_data:
    if item['expiryDate'] == expiry:
        row = {
            'Strike': item['strikePrice'],
        }

        # Call option data
        if 'CE' in item:
            row['CE_OI'] = item['CE']['openInterest']
            row['CE_Change_OI'] = item['CE']['changeinOpenInterest']
            row['CE_Volume'] = item['CE']['totalTradedVolume']
            row['CE_IV'] = item['CE']['impliedVolatility']
            row['CE_LTP'] = item['CE']['lastPrice']
            row['CE_Bid'] = item['CE']['bidprice']
            row['CE_BidQty'] = item['CE']['bidQty']
            row['CE_Ask'] = item['CE']['askPrice']
            row['CE_AskQty'] = item['CE']['askQty']

        # Put option data
        if 'PE' in item:
            row['PE_OI'] = item['PE']['openInterest']
            row['PE_Change_OI'] = item['PE']['changeinOpenInterest']
            row['PE_Volume'] = item['PE']['totalTradedVolume']
            row['PE_IV'] = item['PE']['impliedVolatility']
            row['PE_LTP'] = item['PE']['lastPrice']
            row['PE_Bid'] = item['PE']['bidprice']
            row['PE_BidQty'] = item['PE']['bidQty']
            row['PE_Ask'] = item['PE']['askPrice']
            row['PE_AskQty'] = item['PE']['askQty']

        rows.append(row)

df = pd.DataFrame(rows)
print(df)

# Liquidity analysis - Find most liquid strikes
df['CE_Liquidity_Score'] = df['CE_OI'] + (df['CE_Volume'] * 10)
df['PE_Liquidity_Score'] = df['PE_OI'] + (df['PE_Volume'] * 10)

print("\nMost Liquid Call Strikes:")
print(df.nlargest(5, 'CE_Liquidity_Score')[['Strike', 'CE_OI', 'CE_Volume', 'CE_LTP']])

print("\nMost Liquid Put Strikes:")
print(df.nlargest(5, 'PE_Liquidity_Score')[['Strike', 'PE_OI', 'PE_Volume', 'PE_LTP']])
```

### Advanced: Live Option Chain Monitoring
```python
import time

def monitor_option_chain(symbol="NIFTY", interval=60):
    """
    Monitor option chain in real-time and track OI changes.
    """
    print(f"Monitoring {symbol} option chain (updating every {interval}s)")

    previous_data = None

    while True:
        try:
            # Fetch current data
            data = nse_optionchain_scrapper(symbol)
            spot = data['records']['underlyingValue']

            print(f"\n{symbol} Spot: {spot}")

            # Find ATM strike
            strikes = [item['strikePrice'] for item in data['records']['data']]
            atm_strike = min(strikes, key=lambda x: abs(x - spot))

            # Get ATM option data
            for item in data['records']['data']:
                if item['strikePrice'] == atm_strike:
                    if 'CE' in item and 'PE' in item:
                        print(f"\nATM Strike: {atm_strike}")
                        print(f"CE OI: {item['CE']['openInterest']:,} (Change: {item['CE']['changeinOpenInterest']:+,})")
                        print(f"PE OI: {item['PE']['openInterest']:,} (Change: {item['PE']['changeinOpenInterest']:+,})")
                        print(f"PCR (OI): {item['PE']['openInterest'] / item['CE']['openInterest']:.2f}")
                        break

            time.sleep(interval)

        except KeyboardInterrupt:
            print("\nMonitoring stopped.")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(interval)

# Run monitoring
# monitor_option_chain("NIFTY", interval=60)
```

### Bank NIFTY Example
```python
# Get Bank NIFTY option chain
banknifty_chain = nse_optionchain_scrapper("BANKNIFTY")

spot = banknifty_chain['records']['underlyingValue']
print(f"Bank NIFTY Spot: {spot}")

# Calculate Put-Call Ratio (PCR) using OI
total_ce_oi = 0
total_pe_oi = 0

for item in banknifty_chain['records']['data']:
    if 'CE' in item:
        total_ce_oi += item['CE']['openInterest']
    if 'PE' in item:
        total_pe_oi += item['PE']['openInterest']

pcr = total_pe_oi / total_ce_oi if total_ce_oi > 0 else 0
print(f"PCR (Open Interest): {pcr:.2f}")

if pcr > 1.2:
    print("Market Sentiment: Bullish (High Put writing)")
elif pcr < 0.8:
    print("Market Sentiment: Bearish (High Call writing)")
else:
    print("Market Sentiment: Neutral")
```

---

## 2️⃣ nselib - Clean & Modern API

**Repository:** https://github.com/RuchiTanmay/nselib
**License:** Apache-2.0
**Status:** ✅ Actively maintained

### Features
- ✅ Clean, modern API
- ✅ Full option chain data
- ✅ OI, Change in OI, Volume, IV
- ✅ Multiple expiry support
- ✅ Compact/Full modes

### Installation
```bash
pip install nselib
```

### Quick Start
```python
from nselib import derivatives

# Get live NIFTY option chain
option_chain = derivatives.nse_live_option_chain(
    symbol="NIFTY",
    expiry_date="30-01-2025",  # Optional, defaults to nearest expiry
    oi_mode="full"  # "full" or "compact"
)

print(option_chain)

# Option chain is returned as pandas DataFrame with columns:
# - Strike_Price
# - CALLS_OI, CALLS_Chng_in_OI, CALLS_Volume, CALLS_IV, CALLS_LTP
# - PUTS_OI, PUTS_Chng_in_OI, PUTS_Volume, PUTS_IV, PUTS_LTP
# - And more bid/ask data in "full" mode
```

### Liquidity Analysis with nselib
```python
import pandas as pd

# Get option chain
df = derivatives.nse_live_option_chain("NIFTY", oi_mode="full")

# Filter by liquidity (OI > 10,000 and Volume > 1,000)
liquid_calls = df[
    (df['CALLS_OI'] > 10000) &
    (df['CALLS_Volume'] > 1000)
]

liquid_puts = df[
    (df['PUTS_OI'] > 10000) &
    (df['PUTS_Volume'] > 1000)
]

print("Liquid Call Strikes:")
print(liquid_calls[['Strike_Price', 'CALLS_OI', 'CALLS_Volume', 'CALLS_LTP']])

print("\nLiquid Put Strikes:")
print(liquid_puts[['Strike_Price', 'PUTS_OI', 'PUTS_Volume', 'PUTS_LTP']])

# Calculate bid-ask spread (full mode only)
if 'CALLS_Bid_Price' in df.columns:
    df['CE_Spread'] = df['CALLS_Ask_Price'] - df['CALLS_Bid_Price']
    df['PE_Spread'] = df['PUTS_Ask_Price'] - df['PUTS_Bid_Price']

    print("\nTightest Bid-Ask Spreads (Most Liquid):")
    print(df.nsmallest(10, 'CE_Spread')[['Strike_Price', 'CE_Spread', 'CALLS_OI']])
```

### Get All Available Expiry Dates
```python
# Get expiry dates for NIFTY options
expiry_dates = derivatives.expiry_dates_option_index()
print(f"Available NIFTY expiries: {expiry_dates['NIFTY']}")

# Get Bank NIFTY expiries
print(f"Available Bank NIFTY expiries: {expiry_dates['BANKNIFTY']}")

# Get FinNIFTY expiries (if trading)
print(f"Available FinNIFTY expiries: {expiry_dates.get('FINNIFTY', 'Not available')}")
```

---

## 3️⃣ jugaad-data - Historical + Live

**Repository:** https://github.com/jugaad-py/jugaad-data
**License:** MIT-like
**Status:** ✅ Actively maintained

### Features
- ✅ Historical derivatives data (bhavcopy)
- ✅ Live option chain
- ✅ Clean API with caching
- ✅ Multiple indices support

### Installation
```bash
pip install jugaad-data
```

### Quick Start
```python
from jugaad_data.nse import NSELive

nse = NSELive()

# Get NIFTY option chain
nifty_oc = nse.index_option_chain("NIFTY")

# Get Bank NIFTY option chain
banknifty_oc = nse.index_option_chain("BANKNIFTY")

# Access option chain data
records = nifty_oc['records']['data']

# Filter and analyze
for option in records:
    strike = option['strikePrice']

    if 'CE' in option:
        ce_oi = option['CE']['openInterest']
        ce_volume = option['CE']['totalTradedVolume']
        print(f"Strike {strike} CE: OI={ce_oi:,}, Volume={ce_volume:,}")
```

### Historical Options Data
```python
from jugaad_data.nse import bhavcopy_fno
from datetime import date

# Get historical FNO bhavcopy (end-of-day data)
data = bhavcopy_fno(date(2025, 1, 15))

# Filter for NIFTY options
nifty_options = data[
    (data['SYMBOL'] == 'NIFTY') &
    (data['INSTRUMENT'] == 'OPTIDX')
]

print(nifty_options[['STRIKE_PR', 'OPTION_TYP', 'OPEN_INT', 'CONTRACTS', 'CLOSE']])
```

---

## 4️⃣ nsetools - Derivatives Focus

**Repository:** https://github.com/vsjha18/nsetools
**License:** MIT
**Status:** ✅ Maintained

### Features
- ✅ Derivatives quotes with OI
- ✅ Option chain data
- ✅ Futures data
- ✅ Stock derivatives

### Installation
```bash
pip install nsetools
```

### Quick Start
```python
from nsetools import Nse

nse = Nse()

# Get derivatives quote (includes OI)
quote = nse.get_quote_derivative("NIFTY", type="futures")
print(f"Open Interest: {quote['openInterest']}")
print(f"Change in OI: {quote['changeInOpenInterest']}")
print(f"Traded Volume: {quote['tradedVolume']}")
```

---

## 5️⃣ nsedt - Simple Option Chain API

**Repository:** https://github.com/pratik141/nsedt
**License:** Apache-2.0
**Status:** ✅ Active

### Installation
```bash
pip install nsedt
```

### Quick Start
```python
from nsedt import derivatives

# Get option chain
oc = derivatives.get_option_chain("NIFTY")

# Get specific strike
oc_strike = derivatives.get_option_chain("NIFTY", strike_price="21000")

# Get specific expiry
oc_expiry = derivatives.get_option_chain("NIFTY", expiry_date="30-Jan-2025")

# Get expiry dates
expiries = derivatives.get_option_chain_expdate("NIFTY")
print(expiries)
```

---

## 📊 Liquidity Metrics Explained

### 1. Open Interest (OI)
**What:** Total number of outstanding option contracts
**Importance:** Higher OI = More liquid = Easier to enter/exit
**Threshold:** For NIFTY, OI > 10,000 is considered liquid

### 2. Change in Open Interest (ΔOI)
**What:** Change in OI from previous day
**Interpretation:**
- +ΔOI with price ↑ = Long buildup (Bullish)
- +ΔOI with price ↓ = Short buildup (Bearish)
- -ΔOI with price ↑ = Short covering (Bullish)
- -ΔOI with price ↓ = Long unwinding (Bearish)

### 3. Volume
**What:** Number of contracts traded today
**Importance:** High volume = Active trading = Better execution
**Threshold:** Volume > 1,000 for NIFTY options

### 4. Bid-Ask Spread
**What:** Difference between bid and ask price
**Importance:** Narrow spread = More liquid = Lower transaction cost
**Good spread:** < ₹5 for ATM options

### 5. Implied Volatility (IV)
**What:** Market's expectation of future volatility
**Use:** High IV = Expensive options, Low IV = Cheap options

---

## 🎯 Practical Use Cases

### Use Case 1: Find Most Liquid Strikes
```python
from nsepython import nse_optionchain_scrapper
import pandas as pd

def find_liquid_strikes(symbol="NIFTY", min_oi=10000, min_volume=1000):
    """
    Find most liquid option strikes based on OI and Volume.
    """
    data = nse_optionchain_scrapper(symbol)

    liquid_strikes = []
    for item in data['records']['data']:
        strike = item['strikePrice']

        # Check Call liquidity
        if 'CE' in item:
            if (item['CE']['openInterest'] > min_oi and
                item['CE']['totalTradedVolume'] > min_volume):
                liquid_strikes.append({
                    'Strike': strike,
                    'Type': 'CE',
                    'OI': item['CE']['openInterest'],
                    'Volume': item['CE']['totalTradedVolume'],
                    'LTP': item['CE']['lastPrice']
                })

        # Check Put liquidity
        if 'PE' in item:
            if (item['PE']['openInterest'] > min_oi and
                item['PE']['totalTradedVolume'] > min_volume):
                liquid_strikes.append({
                    'Strike': strike,
                    'Type': 'PE',
                    'OI': item['PE']['openInterest'],
                    'Volume': item['PE']['totalTradedVolume'],
                    'LTP': item['PE']['lastPrice']
                })

    df = pd.DataFrame(liquid_strikes)
    return df.sort_values('OI', ascending=False)

# Use it
liquid = find_liquid_strikes("NIFTY")
print(liquid.head(10))
```

### Use Case 2: Max Pain Calculator
```python
def calculate_max_pain(symbol="NIFTY", expiry=None):
    """
    Calculate Max Pain strike (where most options expire worthless).
    """
    data = nse_optionchain_scrapper(symbol)

    strikes = {}
    for item in data['records']['data']:
        if expiry and item.get('expiryDate') != expiry:
            continue

        strike = item['strikePrice']
        ce_oi = item.get('CE', {}).get('openInterest', 0)
        pe_oi = item.get('PE', {}).get('openInterest', 0)

        strikes[strike] = {'CE_OI': ce_oi, 'PE_OI': pe_oi}

    # Calculate pain at each strike
    pain_values = {}
    for test_strike in strikes.keys():
        pain = 0
        for strike, oi in strikes.items():
            # Call pain: if spot > strike, calls ITM
            if test_strike > strike:
                pain += (test_strike - strike) * oi['CE_OI']
            # Put pain: if spot < strike, puts ITM
            if test_strike < strike:
                pain += (strike - test_strike) * oi['PE_OI']

        pain_values[test_strike] = pain

    # Max pain = strike with minimum total pain
    max_pain_strike = min(pain_values, key=pain_values.get)

    return max_pain_strike, pain_values

# Use it
max_pain, pain_data = calculate_max_pain("NIFTY")
print(f"Max Pain Strike: {max_pain}")
```

### Use Case 3: PCR (Put-Call Ratio) Analysis
```python
def calculate_pcr(symbol="NIFTY", metric="OI"):
    """
    Calculate Put-Call Ratio using OI or Volume.
    metric: "OI" or "Volume"
    """
    data = nse_optionchain_scrapper(symbol)

    total_ce = 0
    total_pe = 0

    for item in data['records']['data']:
        if metric == "OI":
            ce_val = item.get('CE', {}).get('openInterest', 0)
            pe_val = item.get('PE', {}).get('openInterest', 0)
        else:  # Volume
            ce_val = item.get('CE', {}).get('totalTradedVolume', 0)
            pe_val = item.get('PE', {}).get('totalTradedVolume', 0)

        total_ce += ce_val
        total_pe += pe_val

    pcr = total_pe / total_ce if total_ce > 0 else 0

    # Interpretation
    if pcr > 1.2:
        sentiment = "Bullish"
    elif pcr < 0.8:
        sentiment = "Bearish"
    else:
        sentiment = "Neutral"

    return {
        'PCR': pcr,
        'Sentiment': sentiment,
        'Total_CE': total_ce,
        'Total_PE': total_pe
    }

# Use it
pcr_data = calculate_pcr("NIFTY", metric="OI")
print(f"PCR (OI): {pcr_data['PCR']:.2f} - {pcr_data['Sentiment']}")
```

---

## 🎨 Ready-to-Use Analysis Tools

### Tool 1: Python NSE Option Chain Analyzer (GUI)
**Repository:** https://github.com/VarunS2002/Python-NSE-Option-Chain-Analyzer
**License:** GPL-3.0

Full-featured GUI application with:
- Real-time option chain display
- OI analysis charts
- PCR calculations
- Max Pain indicator
- CSV export

```bash
git clone https://github.com/VarunS2002/Python-NSE-Option-Chain-Analyzer
cd Python-NSE-Option-Chain-Analyzer
pip install -r requirements.txt
python NSE_Option_Chain_Analyzer.py
```

### Tool 2: Options OI Plotter
**Repository:** https://github.com/ashok-kollipara/options-oi
**License:** MIT

Plots OI and Change in OI:
```bash
pip install nsepython pandas matplotlib
git clone https://github.com/ashok-kollipara/options-oi
cd options-oi
python plot.py
```

---

## ⚠️ Important Notes

### Rate Limiting
NSE has rate limits on their APIs. To avoid issues:
- Add delays between requests (`time.sleep(1)`)
- Cache data when possible
- Don't hammer the server
- Use session cookies properly

### Data Accuracy
- Option chain data is **near real-time** (15-30 second delay)
- For exact execution, check broker's terminal
- Volume resets daily at market open
- OI updates once daily (EOD for most exchanges)

### Trading Hours
- Live data available only during: **9:15 AM - 3:30 PM IST**
- Pre-market: 9:00 AM - 9:15 AM (limited data)
- After-hours: 3:30 PM - 9:00 PM (post-market orders)

### Legal & Disclaimer
- Data is for **informational purposes only**
- Not investment advice
- Check NSE's terms of use
- Use responsibly and ethically

---

## 🔗 Related KB Documents

- [OpenBB Capabilities](../openbb/capabilities.md) - OpenBB doesn't have Indian options, use these instead
- [Free Tools Ecosystem](free-tools-ecosystem.md) - Complementary analysis tools
- [LLM Analysis Prompts](../strategies/llm-analysis-prompts.md) - Prompts for options analysis

---

## 📚 Additional Resources

### Documentation
- [NSE India Official](https://www.nseindia.com/)
- [NSE F&O Trading Guide](https://www.nseindia.com/products-services/equity-derivatives)
- [Options Greeks Calculator](https://www.nseindia.com/option-chain)

### Learning Resources
- Zerodha Varsity: Options Trading Module
- NSE Academy: Derivatives Certification
- YouTube: Option Chain Analysis tutorials

---

**Research Date:** 2025-01-18
**Sources:** 10+ Python libraries on GitHub
**Verification:** All libraries actively maintained and working
**Best Choice:** **nsepython** for most comprehensive liquidity data
