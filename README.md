# Pairs Trading Algorithm

A quantitative statistical arbitrage system built in Python that identifies 
and validates trading opportunities across 10 correlated stock pairs.

## What it does
- Pulls live daily price data for 10 validated stock pairs
- Calculates a z-score for each pair based on 3 years of historical data
- Prints a morning dashboard with actionable trade signals
- Backtests each pair from 2020 to today to validate historical profitability

## Files
- `dashboard.py` — run every morning to get today's live trade signals
- `pairs.py` — full backtest showing historical P&L for all 10 pairs

## Trade Signal Logic
- Z-score > 2: Strong sell the outperformer, buy the underperformer
- Z-score > 1: Sell the outperformer, buy the underperformer
- Z-score < -1: Buy the underperformer, sell the outperformer
- Z-score < -2: Strong buy the underperformer, sell the outperformer
- Z-score between -1 and 1: No trade

## Validated Pairs & Backtest Results (2020–2026)
| Pair | Tickers | Backtest P&L |
|------|---------|-------------|
| Visa / Mastercard | V, MA | $938 |
| Exxon / Chevron | XOM, CVX | $2,612 |
| Nike / Adidas | NKE, ADDYY | $60,252 |
| McDonald's / Yum Brands | MCD, YUM | $7,744 |
| S&P 500 / Nasdaq | SPY, QQQ | $7,429 |
| AMD / Nvidia | AMD, NVDA | $1,805,710 |
| Uber / Lyft | UBER, LYFT | $331,583 |
| Costco / Walmart | COST, WMT | $237,178 |
| Goldman Sachs / Morgan Stanley | GS, MS | $30,240 |
| Netflix / Disney | NFLX, DIS | $27,910 |

## Methodology
Pairs are selected based on business model similarity and historical 
correlation. The z-score measures how far the current price ratio has 
deviated from its 3-year historical mean. Strategy was backtested across 6 years of data (2020-2026) to vaildate profitability. Trades are entered when the 
z-score exceeds ±1 and closed when it reverts to near zero.

Unprofitable pairs were identified through backtesting and removed. 
The final 10 pairs were all validated as historically profitable before 
being included in the live dashboard. Pairs will be continuously monitored and updated.

## Tech Stack
- Python 3.14
- yfinance — live market data
- pandas — data manipulation
- matplotlib — visualization
- statsmodels — statistical analysis

## How to Run
```bash
pip3 install pandas yfinance numpy matplotlib statsmodels
python3 dashboard.py
```

## Project Status
Active — signals checked and logged daily. Next steps include automated 
alerting, position sizing, and a public newsletter documenting live signals. More pairs will be added as time goes on.

## Author
Built as an independent quantitative finance project to explore 
statistical arbitrage and systematic trading strategies.
