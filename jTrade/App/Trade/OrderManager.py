import App.Trade.FeeModel
import App.Trade.Order
import App.Trade.Position

class OrderManager(object):
    """Order Manager. Responsible for order processing."""

    def __init__(self):
        self.positions = {}

    def place_order(self, order : App.Trade.Order):
        try:
            pos = self.positions.get(order.equity.symbol)
            if not pos:
                self.positions[pos] = App.Trade.Position.Position(order.equity)
            self.positions[pos].place_order(order)
        except Exception as e:
            raise e.with_traceback(e.__traceback__)