# Database Structure

### Quote
Real time instrument quote from Yahoo Finance. For now, columns include:
- symbol (key)
- time (key)
- price 
- change 
- volume 
- avg_volume 
- name 
- exchange 
- market_cap 
- day_high 
- day_low 
- year_high 
- year_low 

### HistPrc
Daily historical price. Source TBD. Columns:
- symbol (key)
- date (key)
- open
- high
- low
- close
- volume

### Financial
Quarterly financial data. Source TBD. There are 2 possible implementations:
1. One big table, each column has prefix (is, cf, bs...). Pro: just one table, as they are together one piece of 
   information. Con: column name messy.
2. Four tables. Pro: easy to understand. Con: 4 tables.

Each entry:
- symbol (key)
- quarter (key)
- number...

### TechSig
Calculated / queried technical signal. Should be daily.
- symbol (key)
- date (key)
- signals...

### FdmtSig
Calculated / queried fundamental signal. Should be quarterly.
- symbol (key)
- quarter (key)
- signals...

### Position
Keeps track of positions and their daily (eod) status.
- symbol (key)
- date (key)
- share
- value
- price
- cost
- pct_ret
- abs_ret

### Trade
Keeps track of trades happened. Since all data are daily, trades are assumed to happen at a day, at the average of
open, high, low, and close.
- symbol (key)
- date (key)
- share
- price