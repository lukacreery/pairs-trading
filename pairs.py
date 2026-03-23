import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
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
start = "2020-01-01"

print("=" * 55)
print("  BACKTEST RESULTS — 2020 to Today")
print("=" * 55)

plt.figure(figsize=(14, 7))

for t1, t2, name in pairs:
    try:
        data = yf.download([t1, t2], start=start, end=end, progress=False)["Close"]
        if t1 not in data.columns or t2 not in data.columns:
            print(f"{name:<30} → ERROR: data missing")
            continue

        normalized = data / data.iloc[0] * 100
        ratio = normalized[t1] / normalized[t2]
        mean = ratio.mean()
        std = ratio.std()
        zscore = (ratio - mean) / std

        position = 0
        pnl = []
        entry_ratio = None

        for i in range(len(zscore)):
            z = zscore.iloc[i]
            v_price = data[t1].iloc[i]
            ma_price = data[t2].iloc[i]

            if position == 0:
                if z > 1:
                    position = -1
                    entry_ratio = v_price / ma_price
                elif z < -1:
                    position = 1
                    entry_ratio = v_price / ma_price
                pnl.append(0)

            elif position == 1:
                current_ratio = v_price / ma_price
                pnl.append((current_ratio - entry_ratio) * 1000)
                if abs(z) < 0.1:
                    position = 0
                    entry_ratio = None

            elif position == -1:
                current_ratio = v_price / ma_price
                pnl.append((entry_ratio - current_ratio) * 1000)
                if abs(z) < 0.1:
                    position = 0
                    entry_ratio = None

        pnl_series = pd.Series(pnl, index=zscore.index)
        cumulative = pnl_series.cumsum()
        total = cumulative.iloc[-1]

        plt.plot(cumulative, label=name)
        print(f"{name:<30} Total P&L: ${total:>8.2f}")

    except Exception as e:
        print(f"{name:<30} → ERROR: {e}")

print("=" * 55)
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
plt.title("Backtest — Cumulative P&L All 10 Pairs (2020 to Today)")
plt.xlabel("Date")
plt.ylabel("Profit / Loss ($)")
plt.legend(fontsize=7)
plt.tight_layout()
plt.show()