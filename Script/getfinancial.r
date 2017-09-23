library('quantmod')

options("getSymbols.warning4.0"=F)
prcs = getSymbols("FB",from="1990-1-1",to="2012-12-31",src="google",auto.assign=F)
prcs = getSymbols("AAPL",src="google",auto.assign=F)
fins = getFinancials('AAPL', auto.assign=F)

