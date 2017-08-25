import datetime
import pandas as pd
from rpy2.robjects import r, pandas2ri
import rpy2.robjects.packages as rpackages
import Data.DB.DBManager
import Data.DB.Table


class QuantMod(object):
    quantmod = rpackages.importr('quantmod')
    pandas2ri.activate()

    @staticmethod
    def EquityHP1d(symbol, start, end):
        try:
            # gets a ndarray
            r('{} = getSymbols("{}",from="{}",to="{}",auto.assign=F)'.format(symbol+'.hp', symbol, start.isoformat(),
                                                                             end.isoformat()))
            # convert to dataframe
            r('{} = data.frame(date=index({}), coredata({}))'.format(symbol+'.hp', symbol+'.hp', symbol+'.hp'))
            hps = pd.DataFrame(r[symbol+'.hp'])
            # convert days since epoch to datetime
            epoch = datetime.date(1970, 1, 1)
            hps.loc[:,'date'] = [epoch+datetime.timedelta(days=int(d)) for d in hps.loc[:,'date']]
            # add column of symbol
            hps['symbol'] = symbol
            # convert column names
            hps.columns = [name.split('.')[-1].lower() for name in hps.columns]
            return hps
            # conn = dm._engine.connect()
            # for i in range(1, hps.shape[0] + 1):
            #     ins = Data.DB.Table.EquityHP1d.insert().values(
            #         symbol=symbol,
            #         date=epoch + datetime.timedelta(days=int(hps['date'][i])),
            #         opn=float(hps[symbol + '.Open'][i]),
            #         high=float(hps[symbol + '.High'][i]),
            #         low=float(hps[symbol + '.Low'][i]),
            #         close=float(hps[symbol + '.Close'][i]),
            #         volume=float(hps[symbol + '.Volume'][i]),
            #         adjusted=float(hps[symbol + '.Adjusted'][i])
            #     )
            #     conn.execute(ins)
            # conn.close()
        except Exception as e:
            raise e.with_traceback(e.__traceback__)


if __name__ == '__main__':
    test = QuantMod.EquityHP1d('MSFT', datetime.date(2000,1,1), datetime.date(2017,8,23))
    dm = Data.DB.DBManager.DBManager()
    dm.insert_df(Data.DB.Table.EquityHP1d, test)