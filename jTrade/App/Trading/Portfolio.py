import App.Trading.FeeModel
import App.Trading.Order
import App.Trading.Position

class Portfolio(object):
    """Portfolio. Responsible for order processing and position tracking."""

    def __init__(self):
        self.positions = {}

    def place_order(self, order : App.Trading.Order):
        try:
            pos = self.positions.get(order.equity.symbol)
            if not pos:
                self.positions[order.equity.symbol] = App.Trading.Position.Position(order.equity)
            self.positions[order.equity.symbol].place_order(order)
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def value(self, date):
        try:
            return sum(p.value(date) for p in self.positions.values())
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

if __name__ == '__main__':
    import datetime
    import Core.Instrument.Equity
    today = datetime.date(2017,8,30)
    port = Portfolio()

    eq = Core.Instrument.Equity.Equity('AAPL', 'Apple, Inc.')
    eq.get_hp()
    fm = App.Trading.FeeModel.FixedFlat(0)
    od = App.Trading.Order.Order(eq, today, 100, eq.day_avg(today), fm)
    print(port.positions)
    port.place_order(od)
    print(port.positions)
    print(port.positions['AAPL'].order_history)