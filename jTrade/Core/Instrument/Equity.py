import pandas as pd

import Data.Table
import Data.Table
from Data.DBManager import dbmanager


class Equity(object):
    """Equity class."""

    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
        self.hp = pd.DataFrame()
        self.fin_stmt = pd.DataFrame()

    def get_hp(self, start=None, end=None):
        """Gets daily historical price from current DB.

        :param start:
        :param end:
        :return:
        """
        try:
            if not start and not end:
                fil = {('symbol', '='): self.symbol}
            elif not start :
                fil = {'&': {('symbol', '='): self.symbol,
                             ('date', '<='): end}}
            elif not end:
                fil = {'&': {('symbol', '='): self.symbol,
                             ('date', '>='): start}}
            else:
                fil = {'&': {('symbol', '='): self.symbol,
                             ('date', '>='): start,
                             ('date', '<='): end}}
            hp = dbmanager.select(Data.Table.EquityHP, fil)
            self.hp = hp
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def get_financial(self):
        try:
            pass
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def open(self, date):
        try:
            return float(self.hp.loc[date, 'open'])
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def high(self, date):
        try:
            return float(self.hp.loc[date, 'high'])
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def low(self, date):
        try:
            return float(self.hp.loc[date, 'low'])
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def close(self, date):
        try:
            return float(self.hp.loc[date, 'close'])
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def day_avg(self, date):
        try:
            return (self.open(date) + self.high(date) + self.low(date) + self.close(date)) / 4
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

if __name__ == '__main__':
    aapl = Equity('AAPL', 'Apple, Inc.')
    aapl.get_hp()