from App.Screening.Screener import Screener
from Core.Signal.Tech import *

class MACD(Screener):
    def screen(self, equity):
        macd, macdsignal, macdhist = MACD(equity)