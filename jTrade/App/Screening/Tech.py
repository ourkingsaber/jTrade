from jTrade.App.Screening.Screener import Screener
from jTrade.Core.Signal.Tech import *

class MACD(Screener):
    def screen(self, equity):
        macd, macdsignal, macdhist = MACD(equity)