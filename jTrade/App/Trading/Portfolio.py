import jTrade.App.Trading.FeeModel as FeeModel
import jTrade.App.Trading.Order as Order
import jTrade.App.Trading.Position as Position

class Portfolio(object):
    """Portfolio. Responsible for order processing and position tracking."""

    def __init__(self):
        self.positions = {}

    def place_order(self, order : jTrade.App.Trading.Order):
        pos = self.positions.get(order.equity.symbol)
        if not pos:     # establish new pos if not exist
            self.positions[order.equity.symbol] = jTrade.App.Trading.Position.Position(order.equity)
        self.positions[order.equity.symbol].place_order(order)

    def value(self, date):
        return sum(p.value(date) for p in self.positions.values())


if __name__ == '__main__':
    import datetime
    import jTrade.Core.Instrument.Equity as Equity
    today = datetime.date(2017,8,30)
    port = Portfolio()

    eq = Equity.Equity('AAPL')
    eq.get_hp()
    fm = FeeModel.FixedFlat(0)
    od = Order.Order(eq, today, 100, eq.day_avg(today), fm)
    print(port.positions)
    port.place_order(od)
    print(port.positions)
    print(port.positions['AAPL'].order_history)