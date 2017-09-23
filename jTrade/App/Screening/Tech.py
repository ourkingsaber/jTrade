from App.Screening.Screener import Screener
from Core.Signal.Tech import *

class MACD(Screener):
    def screen(self, equity):
        try:
            macd, macdsignal, macdhist = MACD(equity)
        except Exception as e:
            raise e.with_traceback(e.__traceback__)