# Data Source

Here are the data we need.

## Price

- Historical daily OHLC data for US equities.
- Best Source should be Quandl.
- There is a python package to interact with server.

## Financial Statements

- Quandl has annual fundamental data available. This is hard to use.
- Intrino has quarterly standardized financial data, but with limit of 500 calls per day for free tier
  Paid tier solves this problem. $100 a month (I probably need one month).
- Only web api.
- http://docs.intrinio.com/#standardized-financials

Update - got Developer plan for 6 months, great! It includes:
- US Public Company Security Master Data Feed
- US Public Company Financial Data Feed
- Sector & Industry Data Feed
- IEX Real-Time Pricing Feed Web Socket with Connection Limit
- US Insider Transactions & Ownership
- US Institutional Holdings