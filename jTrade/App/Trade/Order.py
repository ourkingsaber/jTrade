import App.Trade.FeeModel

class Order(object):

    def __init__(self, symbol, date, share, price, fee_model):
        self.symbol = symbol
        self.date = date
        self.share = share
        self.price = price
        self.fee = fee_model.calculate(share, price)