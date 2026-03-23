import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

pairs = [
    ("V", "MA", "Visa / Mastercard"),
    ("XOM", "CVX", "Exxon / Chevron"),
    ("NKE", "ADDYY", "Nike / Adidas"),
    ("MCD", "YUM", "McDonald's / Yum Brands"),
    ("SPY", "QQQ", "S&P 500 / Nasdaq"),
    ("AMD", "NVDA", "AMD / Nvidia"),
    ("UBER", "LYFT", "Uber / Lyft"),
    ("COST", "WMT", "Costco / Walmart"),
    ("GS", "MS", "Goldman Sachs / Morgan Stanley"),
    ("NFLX", "DIS", "Netflix / Disney"),
]

end = datetime.today().strftime("%Y-%m-%d")
start = (datetime.today() - timedelta(days=365*3)).strftime("%Y-%m-%d")

print("=" * 55)
print(f"  PAIRS TRADING DASHBOARD — {datetime.today().strftime('%B %d, %Y')}")
print("=" * 55)

for t1, t2, name in pairs:
    try:
        data = yf.download([t1, t2], start=start, end=end, progress=False)["Close"]
        if t1 not in data.columns or t2 not in data.columns:
            print(f"{name:<30} → ERROR: data missing")
            continue

        normalized = data / data.iloc[0] * 100
        ratio = normalized[t1] / normalized[t2]
        zscore = (ratio - ratio.mean()) / ratio.std()
        z = zscore.iloc[-1]

        if z > 2:
            signal = f"STRONG SELL {t1} / BUY {t2}"
        elif z > 1:
            signal = f"SELL {t1} / BUY {t2}"
        elif z < -2:
            signal = f"STRONG BUY {t1} / SELL {t2}"
        elif z < -1:
            signal = f"BUY {t1} / SELL {t2}"
        else:
            signal = "No trade"

        print(f"{name:<30} Z: {z:+.2f}   → {signal}")

    except Exception as e:
        print(f"{name:<30} → ERROR: {e}")

print("=" * 55)