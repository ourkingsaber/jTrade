# Modules

The system has 4 modules:
- Core: hanldes indicator calculation, trading recording...
- Data: handles all data
- App: handles strategies.
- UI: what?

The tasks are:
1. Get data - defer this to quantmod in R. use rpy2. Still, need to store data in SQL. This over Yahoo finance and 
   individual sources is only the convenience.
2. Calculate analytics / indicators - use TAlib
3. Form strategy based on indicators. Implement this, such as filters for selecting stocks, buy and sell timing, 
   stock / option combining strategies.