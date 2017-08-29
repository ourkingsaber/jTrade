import datetime
import pandas as pd
from rpy2.robjects import r, pandas2ri
import rpy2.robjects.packages as rpackages


class QuantMod(object):
    """Fetches data using quantmod, an R package."""

    quantmod = rpackages.importr('quantmod')
    pandas2ri.activate()

    @staticmethod
    def EquityHP(symbol, start, end):
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
        except Exception as e:
            raise e.with_traceback(e.__traceback__)


if __name__ == '__main__':
    from Data.DB.DBManager import dbmanager
    test = QuantMod.EquityHP('MSFT', datetime.date(2017, 8, 1), datetime.date(2017, 8, 23))
    print(test)
    # dbmanager.insert_df(Data.DB.Table.EquityHP, test)