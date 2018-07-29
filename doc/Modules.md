# Modules

The system has 4 modules:
- Core: hanldes indicator calculation, trading recording...
- Data: handles all data
- App: handles strategies.
- UI: what?

The tasks are:
1. Get data - defer this to quantmod in R. use rpy2 and quantmod. Still, need to store data in SQL. This over Yahoo finance and 
   individual sources is only the convenience.
2. Calculate analytics / indicators - use TAlib. More complex indicators - python modules.
3. Form strategy based on indicators. Implement this, such as filters for selecting stocks, buy and sell timing, 
   stock / option combining strategies. Use sklearn to optimize.
4. Potentially, use QuantLib to do option analysis. Fixed income is too large to worry about.