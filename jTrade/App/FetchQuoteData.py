
import Data.DB.DBManager
import Data.DB.ORM
import Data.Fetch.Query
import Util.Const

quotes_data = Data.Fetch.Query.Yahoo.quote(['AAPL', 'MSFT'])

dm = Data.DB.DBManager.DBManager(Util.Const.LOCAL_DEV_INFO)

quotes = []
for q in quotes_data.values():
    quotes.append(Data.DB.ORM.EquityQuote(**q))

dm.add(quotes)