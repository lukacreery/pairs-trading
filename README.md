# Pairs Trading Algorithm

A quantitative pairs trading system built in Python that identifies 
statistical arbitrage opportunities across 10 correlated stock pairs.

## What it does
- Pulls live daily price data for 10 carefully selected stock pairs
- Calculates a z-score for each pair based on 3 years of historical data
- Prints a morning dashboard with actionable trade signals
- Identifies when two correlated stocks have diverged beyond normal ranges

## Trade Signal Logic
- Z-score > 2: Strong sell the outperformer, buy the underperformer
- Z-score > 1: Sell the outperformer, buy the underperformer
- Z-score < -1: Buy the underperformer, sell the outperformer
- Z-score < -2: Strong buy the underperformer, sell the outperformer
- Z-score between -1 and 1: No trade

## Pairs Monitored
| Pair | Tickers |
|------|---------|
| Visa / Mastercard | V, MA |
| Coca-Cola / Pepsi | KO, PEP |
| JPMorgan / Bank of America | JPM, BAC |
| Exxon / Chevron | XOM, CVX |
| Nike / Adidas | NKE, ADDYY |
| McDonald's / Yum Brands | MCD, YUM |
| Apple / Microsoft | AAPL, MSFT |
| Amazon / Walmart | AMZN, WMT |
| Gold / Silver | GLD, SLV |
| S&P 500 / Nasdaq | SPY, QQQ |

## Tech Stack
- Python 3.14
- yfinance — live market data
- pandas — data manipulation
- matplotlib — visualization
- statsmodels — statistical analysis

## How to Run
```bash
pip3 install pandas yfinance numpy matplotlib statsmodels
python3 pairs.py
```

## Project Status
Active — signals checked and logged daily. Strategy being expanded 
with backtesting, additional pairs, and automated alerting.

## Author
Built as an independent quantitative finance project to explore 
statistical arbitrage and systematic trading strategies.
