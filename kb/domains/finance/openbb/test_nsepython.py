#!/usr/bin/env python3
"""
Test script for nsepython - NIFTY Options Data
Verified working: 2025-01-18
"""

from nsepython import nse_optionchain_scrapper

def test_nifty_option_chain():
    """Fetch and display NIFTY option chain with liquidity metrics."""

    print("Fetching NIFTY option chain...\n")
    data = nse_optionchain_scrapper("NIFTY")

    # Get spot price
    spot = data['records']['underlyingValue']
    print(f"NIFTY Spot: ₹{spot:,.2f}")

    # Get available expiries
    expiries = data['records']['expiryDates']
    print(f"Available Expiries: {expiries[:5]}")

    # Find ATM strike
    option_data = data['records']['data']
    strikes = [item['strikePrice'] for item in option_data
               if 'CE' in item and 'PE' in item]
    atm_strike = min(strikes, key=lambda x: abs(x - spot))

    print(f"\nATM Strike: {atm_strike}")

    # Display ATM option data
    for item in option_data:
        if item['strikePrice'] == atm_strike and 'CE' in item and 'PE' in item:

            print(f"\n{'='*50}")
            print(f"ATM CALL (Strike {atm_strike})")
            print(f"{'='*50}")
            print(f"Open Interest:     {item['CE']['openInterest']:>15,.0f}")
            print(f"Change in OI:      {item['CE']['changeinOpenInterest']:>+15,.0f}")
            print(f"Volume:            {item['CE']['totalTradedVolume']:>15,.0f}")
            print(f"Last Price:        ₹{item['CE']['lastPrice']:>14.2f}")
            print(f"Bid:               ₹{item['CE']['bidprice']:>14.2f} x {item['CE']['bidQty']}")
            print(f"Ask:               ₹{item['CE']['askPrice']:>14.2f} x {item['CE']['askQty']}")
            print(f"Implied Volatility: {item['CE']['impliedVolatility']:>14.2f}%")

            print(f"\n{'='*50}")
            print(f"ATM PUT (Strike {atm_strike})")
            print(f"{'='*50}")
            print(f"Open Interest:     {item['PE']['openInterest']:>15,.0f}")
            print(f"Change in OI:      {item['PE']['changeinOpenInterest']:>+15,.0f}")
            print(f"Volume:            {item['PE']['totalTradedVolume']:>15,.0f}")
            print(f"Last Price:        ₹{item['PE']['lastPrice']:>14.2f}")
            print(f"Bid:               ₹{item['PE']['bidprice']:>14.2f} x {item['PE']['bidQty']}")
            print(f"Ask:               ₹{item['PE']['askPrice']:>14.2f} x {item['PE']['askQty']}")
            print(f"Implied Volatility: {item['PE']['impliedVolatility']:>14.2f}%")

            # Calculate PCR
            pcr = item['PE']['openInterest'] / item['CE']['openInterest']
            print(f"\nPCR (Open Interest): {pcr:.2f}")

            if pcr > 1.2:
                sentiment = "Bullish"
            elif pcr < 0.8:
                sentiment = "Bearish"
            else:
                sentiment = "Neutral"
            print(f"Market Sentiment: {sentiment}")

            break

    print(f"\n{'='*50}")
    print("✅ nsepython is working perfectly!")
    print(f"{'='*50}")


def test_banknifty():
    """Quick test for Bank NIFTY."""

    print("\n\nFetching Bank NIFTY option chain...\n")
    data = nse_optionchain_scrapper("BANKNIFTY")

    spot = data['records']['underlyingValue']
    print(f"Bank NIFTY Spot: ₹{spot:,.2f}")

    # Calculate total PCR
    total_ce_oi = 0
    total_pe_oi = 0

    for item in data['records']['data']:
        if 'CE' in item:
            total_ce_oi += item['CE']['openInterest']
        if 'PE' in item:
            total_pe_oi += item['PE']['openInterest']

    pcr = total_pe_oi / total_ce_oi if total_ce_oi > 0 else 0
    print(f"Total PCR (OI): {pcr:.2f}")

    if pcr > 1.2:
        print("Overall Sentiment: Bullish 📈")
    elif pcr < 0.8:
        print("Overall Sentiment: Bearish 📉")
    else:
        print("Overall Sentiment: Neutral ⚖️")


if __name__ == "__main__":
    try:
        test_nifty_option_chain()
        test_banknifty()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
