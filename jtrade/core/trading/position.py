import datetime
from collections import OrderedDict

import jtrade.core.trading.fee_model as FeeModel
import jtrade.core.instrument.equity as Equity
import jtrade.data.table as Table
import jtrade.util.convert as Convert
from jtrade.data.db_manager import dbmanager


class Position(object):
    """Position class."""

    def __init__(self, equity : Equity):
        self.equity = equity
        self.share = 0
        self.cost = 0
        self.real_gain = 0
        self.current_date = None
        self.bal_history = OrderedDict()
        self.order_history = OrderedDict()

    def place_order(self, order : order.Order):
        assert self.equity is order.equity
        if self.share * order.share >= 0:       # add position
            self.cost += order.total
        else:                                   # in the direction of closing out position
            self.real_gain -= order.total - self.avg_cost() * order.share
            self.cost *= (self.share + order.share) / self.share
        self.share += order.share
        self.current_date = order.date
        #todo: saving to DB should be separate.
        self.order_history[order.date] = {
            'symbol': order.equity.symbol,
            'date': order.date,
            'share': order.share,
            'price': order.price,
            'fee': order.fee,
            'total': order.total
        }

    def save_balance(self):
        self.bal_history[self.current_date] = {
            'symbol': self.equity.symbol,
            'date': self.current_date,
            'share': self.share,
            'price': self.equity.price,
            'value': self.value(),
            'cost': self.cost,
            'real_gain': self.real_gain
        }

    def value(self):
        return self.equity.price * self.share

    def avg_cost(self):
        if self.share == 0:
            return 0
        return self.cost / self.share

    def get_balance_history(self, start=None):
        if not start:
            filtr = {('symbol', '='): self.equity.symbol}
        else:
            filtr = {'&': {('symbol', '='): self.equity.symbol,
                           ('date', '>='): start}}
        hist_df = dbmanager.select(Table.Position, filtr)
        self.bal_history = Convert.dataframe_to_ordereddict(hist_df)

    def get_order_history(self, start=None):
        if not start:
            filtr = {('symbol', '='): self.equity.symbol}
        else:
            filtr = {'&': {('symbol', '='): self.equity.symbol,
                           ('date', '>='): start}}
        hist_df = dbmanager.select(Table.Order, filtr)
        self.order_history = Convert.dataframe_to_ordereddict(hist_df)


if __name__ == '__main__':
    e = Equity.Equity('AAPL')
    p = Position(e)
    fm = FeeModel.FixedFlat(10)
    o = order.Order(e, datetime.date(2017, 1, 1), 100, 100, fm)
    p.place_order(o)
    e.price = 100
    p.save_balance()
    print(Convert.ordereddict_to_dataframe(p.order_history))
    print(Convert.ordereddict_to_dataframe(p.bal_history))
    o = order.Order(e, datetime.date(2017, 1, 2), -50, 100, fm)
    p.place_order(o)
    e.price = 112
    p.save_balance()
    print(Convert.ordereddict_to_dataframe(p.order_history))
    print(Convert.ordereddict_to_dataframe(p.bal_history))
    o = order.Order(e, datetime.date(2017, 1, 3), 50, 120, fm)
    p.place_order(o)
    e.price = 122
    p.save_balance()
    print(Convert.ordereddict_to_dataframe(p.order_history))
    print(Convert.ordereddict_to_dataframe(p.bal_history))
    o = order.Order(e, datetime.date(2017, 1, 4), -100, 120, fm)
    p.place_order(o)
    e.price = 112
    p.save_balance()
    print(Convert.ordereddict_to_dataframe(p.order_history))
    print(Convert.ordereddict_to_dataframe(p.bal_history))