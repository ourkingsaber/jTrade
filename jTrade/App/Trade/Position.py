import pandas as pd
import Core.Instrument.Equity
import Data.DB.DBManager
import Data.DB.Table

class Position(object):
    """Position class."""

    def __init__(self, equity : Core.Instrument.Equity):
        self.equity = equity
        self.bal_history = pd.DataFrame()
        self.order_history = pd.DataFrame()

    def get_balance_history(self, start=None):
        try:
            if not start:
                filtr = {('symbol', '='): self.equity.symbol}
            else:
                filtr = {'&': {('symbol', '='): self.equity.symbol,
                               ('date', '>='): start}}
            dm = Data.DB.DBManager.DBManager()
            hist_df = dm.select(Data.DB.Table.Position, filtr)
            self.bal_history = hist_df
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def get_order_history(self, start=None):
        try:
            if not start:
                filtr = {('symbol', '='): self.equity.symbol}
            else:
                filtr = {'&': {('symbol', '='): self.equity.symbol,
                               ('date', '>='): start}}
            dm = Data.DB.DBManager.DBManager()
            hist_df = dm.select(Data.DB.Table.Order, filtr)
            self.order_history = hist_df
        except Exception as e:
            raise e.with_traceback(e.__traceback__)