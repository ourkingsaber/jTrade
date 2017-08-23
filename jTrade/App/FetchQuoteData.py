
import Data.DB.DBManager
import Data.DB.ORM
import Util.Const

quotes_data = Data.DB.ORM.EquityQuote.query_yahoo(['AAPL', 'MSFT'])

dm = Data.DB.DBManager.DBManager(Util.Const.LOCAL_DEV_INFO)

quotes = []
for q in quotes_data.values():
    quotes.append(Data.DB.ORM.EquityQuote(**q))

dm.add(quotes)