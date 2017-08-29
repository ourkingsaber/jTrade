import datetime
from collections import OrderedDict
import pandas as pd
import App.Trade.FeeModel
import Core.Instrument.Equity
from Data.DB.DBManager import dbmanager

class Order(object):
    """Order class"""

    def __init__(self, equity, date, share, price, fee_model):
        self.equity = equity
        self.date = date
        self.share = share
        self.price = price
        self.fee = fee_model.calculate(share, price)
        self.total = self.share * self.price + self.fee

    def to_df(self):
        try:
            od = OrderedDict([
                ('symbol', self.equity.symbol),
                ('date', self.date),
                ('share', self.share),
                ('price', self.price),
                ('fee', self.fee),
                ('total', self.total)
            ])
            df = pd.DataFrame(od, index=[self.date])
            return df
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def save_to_db(self):
        try:
            pass
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

if __name__ == '__main__':
    test = Core.Instrument.Equity.Equity('AAPL', 'Apple, Inc.')
    fm = App.Trade.FeeModel.FixedFlat(100)
    a = Order(test, datetime.date.today(), 100, 50, fm)
    print(a.total)
    print(a.to_df())