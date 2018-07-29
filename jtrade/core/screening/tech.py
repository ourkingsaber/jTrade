from jtrade.core.screening import Screener
from jtrade.core.signal.tech import *

class MACD(Screener):
    def screen(self, equity):
        macd, macdsignal, macdhist = MACD(equity)