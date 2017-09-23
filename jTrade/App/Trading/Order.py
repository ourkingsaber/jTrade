import datetime
from collections import OrderedDict

import pandas as pd

import App.Trading.FeeModel
import Core.Instrument.Equity


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

    # todo
    def save_to_db(self):
        pass

if __name__ == '__main__':
    test = Core.Instrument.Equity.Equity('AAPL')
    fm = App.Trading.FeeModel.FixedFlat(100)
    a = Order(test, datetime.date.today(), 100, 50, fm)
    print(a.total)
    print(a.to_df())