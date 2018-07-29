from jTrade.core.screening import Screener
from jTrade.core.signal.tech import *

class MACD(Screener):
    def screen(self, equity):
        macd, macdsignal, macdhist = MACD(equity)