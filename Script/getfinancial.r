library('quantmod')

options("getSymbols.warning4.0"=FALSE)
prcs = getSymbols("AAPL",from="1990-1-1",to="2012-12-31",auto.assign=F)
fins = getFinancials('AAPL', from="1990-1-1",to="2012-12-31",auto.assign = FALSE)

