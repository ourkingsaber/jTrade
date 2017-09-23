import pandas as pd

import Data.Table
import Data.Table
from Data.DBManager import dbmanager


class Equity(object):
    """Equity class."""

    def __init__(self, symbol):
        self.symbol = symbol
        self.hp = pd.DataFrame()
        self.fin_stmt = pd.DataFrame()

    def get_hp(self, start=None, end=None):
        """Gets daily historical price from current DB.

        :param start:
        :param end:
        :return:
        """
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

    def get_financial(self):
        pass

    def open(self, date):
        return float(self.hp.loc[date, 'open'])

    def high(self, date):
        return float(self.hp.loc[date, 'high'])

    def low(self, date):
        return float(self.hp.loc[date, 'low'])

    def close(self, date):
        return float(self.hp.loc[date, 'close'])

    def day_avg(self, date):
        return (self.open(date) + self.high(date) + self.low(date) + self.close(date)) / 4

if __name__ == '__main__':
    aapl = Equity('AAPL')
    aapl.get_hp()