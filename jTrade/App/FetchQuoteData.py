
import Data.Query.Processor
import Data.DBManager
import Data.ORM
import Util.Const

quotes_data = Data.Query.Processor.Quote(['AAPL', 'MSFT'])

dm = Data.DBManager.DBManager(Util.Const.LOCAL_DEV_INFO)

quotes = []
for q in quotes_data.obj_dict.values():
    quotes.append(Data.ORM.Quote(**q))

dm.add(quotes)