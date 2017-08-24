import datetime
import numpy as np
import talib
import Data.DB.DBManager
import Data.DB.Table
import Util.Const

class Equity(object):
    """Equity class."""

    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name
        self.hp1d = np.array([])
        self.fin_stmt = np.array([])

    def get_hp1d(self, start=None, end=None, conn=Util.Const.LOCAL_DEV_INFO):
        try:
            if not start:
                start = datetime.date(1900,1,1)
            if not end:
                end = datetime.date.today() - datetime.timedelta(days=1)
            dm = Data.DB.DBManager.DBManager(conn)
            fil = {'&': {('symbol', '='): self.symbol,
                         ('date', '>='): start,
                         ('date', '<='): end}}
            hp1d = dm.select(Data.DB.Table.EquityHP1d, fil)
            self.hp1d = hp1d
        except Exception as e:
            raise e.with_traceback(e.__traceback__)


# ========== TECH OVERLAP INDICATORS **START** ==========
    def BBANDS(self, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0):
        """
        Bollinger Bands
        :param timeperiod:
        :param nbdevup:
        :param nbdevdn:
        :param matype:
        :return:
        """
        try:
            close = np.array(self.hp1d[:,Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            upperband, middleband, lowerband = talib.BBANDS(close, timeperiod=timeperiod, nbdevup=nbdevup, nbdevdn=nbdevdn, matype=matype)
            return upperband, middleband, lowerband
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def DEMA(self, timeperiod=30):
        """
        Double Exponential Moving Average
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:,Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.DEMA(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def EMA(self, timeperiod=30):
        """
        Exponential Moving Average

        NOTE: The EMA function has an unstable period.
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:,Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.EMA(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def HT_TRENDLINE(self):
        """
        Hilbert Transform - Instantaneous Trendline

        NOTE: The HT_TRENDLINE function has an unstable period.
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.HT_TRENDLINE(close)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def KAMA(self, timeperiod=30):
        """
        Kaufman Adaptive Moving Average

        NOTE: The KAMA function has an unstable period.
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.KAMA(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def MA(self, timeperiod=30, matype=0):
        """
        Moving average
        :param timeperiod:
        :param matype:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.MA(close, timeperiod=timeperiod, matype=matype)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def MAMA(self, fastlimit=0, slowlimit=0):
        """
        MESA Adaptive Moving Average

        NOTE: The MAMA function has an unstable period.
        :param fastlimit:
        :param slowlimit:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            mama, fama = talib.MAMA(close, fastlimit=fastlimit, slowlimit=slowlimit)
            return mama, fama
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def MAVP(self, periods, minperiod=2, maxperiod=30, matype=0):
        """
        Moving average with variable period
        :param periods:
        :param minperiod:
        :param maxperiod:
        :param matype:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.MAVP(close, periods, minperiod=minperiod, maxperiod=maxperiod, matype=matype)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def MIDPOINT(self, timeperiod=14):
        """
        MidPoint over period
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.MIDPOINT(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def MIDPRICE(self, timeperiod=14):
        """
        Midpoint Price over period
        :param timeperiod:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            real = talib.MIDPRICE(high, low, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def SAR(self, acceleration=0, maximum=0):
        """
        Parabolic SAR
        :param acceleration:
        :param maximum:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            real = talib.SAR(high, low, acceleration=acceleration, maximum=maximum)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def SAREXT(self, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0, accelerationmaxlong=0,
               accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0):
        """
        Parabolic SAR - Extended
        :param startvalue:
        :param offsetonreverse:
        :param accelerationinitlong:
        :param accelerationlong:
        :param accelerationmaxlong:
        :param accelerationinitshort:
        :param accelerationshort:
        :param accelerationmaxshort:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            real = talib.SAREXT(high, low, startvalue=startvalue, offsetonreverse=offsetonreverse, accelerationinitlong=accelerationinitlong,
                                accelerationlong=accelerationlong, accelerationmaxlong=accelerationmaxlong, accelerationinitshort=accelerationinitshort,
                                accelerationshort=accelerationshort, accelerationmaxshort=accelerationmaxshort)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def SMA(self, timeperiod=30):
        """
        Simple Moving Average
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.SMA(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def T3(self, timeperiod=5, vfactor=0):
        """
        Triple Exponential Moving Average (T3)

        NOTE: The T3 function has an unstable period.
        :param timeperiod:
        :param vfactor:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.T3(close, timeperiod=timeperiod, vfactor=vfactor)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def TEMA(self, timeperiod=30):
        """
        Triple Exponential Moving Average
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.TEMA(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def TRIMA(self, timeperiod=30):
        """
        Triangular Moving Average
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.TRIMA(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def WMA(self, timeperiod=30):
        """
        Weighted Moving Average
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.WMA(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)
# ========== TECH OVERLAP INDICATORS **END** ==========


# ========== TECH MOMENTUM INDICATORS **START** ==========
    def ADX(self, timeperiod=14):
        """
        Average Directional Movement Index

        NOTE: The ADX function has an unstable period.
        :param timeperiod:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.ADX(high, low, close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def ADXR(self, timeperiod=14):
        """
        Average Directional Movement Index Rating

        NOTE: The ADXR function has an unstable period.
        :param timeperiod:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.ADXR(high, low, close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def APO(self, fastperiod=12, slowperiod=26, matype=0):
        """
        Absolute Price Oscillator
        :param fastperiod:
        :param slowperiod:
        :param matype:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.APO(close, fastperiod=fastperiod, slowperiod=slowperiod, matype=matype)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def AROON(self, timeperiod=14):
        """
        Aroon
        :param timeperiod:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            aroondown, aroonup = talib.AROON(high, low, timeperiod=timeperiod)
            return aroondown, aroonup
        except Exception as e:
            raise e.with_traceback(e.__traceback__)\

    def AROONOSC(self, timeperiod=14):
        """
        Aroon Oscillator
        :param timeperiod:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            real = talib.AROONOSC(high, low, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def BOP(self):
        """
        Balance Of Power
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.BOP(opn, high, low, close)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CCI(self, timeperiod=14):
        """
        Commodity Channel Index
        :param timeperiod:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.CCI(high, low, close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CMO(self, timeperiod=14):
        """
        Chande Momentum Oscillator

        NOTE: The CMO function has an unstable period.
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.CMO(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def DX(self, timeperiod=14):
        """
        Directional Movement Index

        NOTE: The DX function has an unstable period.
        :param timeperiod:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.DX(high, low, close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def MACD(self, fastperiod=12, slowperiod=26, signalperiod=9):
        """
        Moving Average Convergence/Divergence
        :param fastperiod:
        :param slowperiod:
        :param signalperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            macd, macdsignal, macdhist = talib.MACD(close, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)
            return macd, macdsignal, macdhist
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def MACDEXT(self, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0):
        """
        MACD with controllable MA type
        :param fastperiod:
        :param fastmatype:
        :param slowperiod:
        :param slowmatype:
        :param signalperiod:
        :param signalmatype:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            macd, macdsignal, macdhist = talib.MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0,
                                                       signalperiod=9, signalmatype=0)
            return macd, macdsignal, macdhist
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def MACDFIX(self, signalperiod=9):
        """
        Moving Average Convergence/Divergence Fix 12/26
        :param signalperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            macd, macdsignal, macdhist = talib.MACDFIX(close, signalperiod=signalperiod)
            return macd, macdsignal, macdhist
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def MFI(self, timeperiod=14):
        """
        Money Flow Index

        NOTE: The MFI function has an unstable period.
        :param timeperiod:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            volume = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('volume')], dtype='f8')
            real = talib.MFI(high, low, close, volume, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def MINUS_DI(self, timeperiod=14):
        """
        Minus Directional Indicator

        NOTE: The MINUS_DI function has an unstable period.
        :param timeperiod:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.MINUS_DI(high, low, close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def MINUS_DM(self, high, low, timeperiod=14):
        """
        Minus Directional Movement

        NOTE: The MINUS_DM function has an unstable period.
        :param high:
        :param low:
        :param timeperiod:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            real = talib.MINUS_DM(high, low, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def MOM(self, timeperiod=10):
        """
        Momentum
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.MOM(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)\

    def PLUS_DI(self, timeperiod=14):
        """
        Plus Directional Indicator

        NOTE: The PLUS_DI function has an unstable period.
        :param timeperiod:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.PLUS_DI(high, low, close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def PLUS_DM(self, timeperiod=14):
        """
        Plus Directional Movement

        NOTE: The PLUS_DM function has an unstable period.
        :param timeperiod:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            real = talib.PLUS_DM(high, low, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def PPO(self, fastperiod=12, slowperiod=26, matype=0):
        """
        Percentage Price Oscillator
        :param fastperiod:
        :param slowperiod:
        :param matype:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.PPO(close, fastperiod=fastperiod, slowperiod=slowperiod, matype=matype)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def ROC(self, timeperiod=10):
        """
        Rate of change : ((price/prevPrice)-1)*100
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.ROC(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def ROCP(self, timeperiod=10):
        """
        Rate of change Percentage: (price-prevPrice)/prevPrice
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.ROCP(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def ROCR(self, timeperiod=10):
        """
        Rate of change ratio: (price/prevPrice)
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.ROCR(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def ROCR100(self, timeperiod=10):
        """
        Rate of change ratio 100 scale: (price/prevPrice)*100
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.ROCR100(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def RSI(self, timeperiod=14):
        """
        Relative Strength Index

        NOTE: The RSI function has an unstable period.
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.RSI(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def STOCH(self, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0):
        """
        Stochastic
        :param fastk_period:
        :param slowk_period:
        :param slowk_matype:
        :param slowd_period:
        :param slowd_matype:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            slowk, slowd = talib.STOCH(high, low, close, fastk_period=fastk_period, slowk_period=slowk_period,
                                       slowk_matype=slowk_matype, slowd_period=slowd_period, slowd_matype=slowd_matype)
            return slowk, slowd
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def STOCHF(self, fastk_period=5, fastd_period=3, fastd_matype=0):
        """
        Stochastic Fast
        :param fastk_period:
        :param fastd_period:
        :param fastd_matype:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            fastk, fastd = talib.STOCHF(high, low, close, fastk_period=fastk_period, fastd_period=fastd_period,
                                        fastd_matype=fastd_matype)
            return fastk, fastd
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def STOCHRSI(self, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0):
        """
        Stochastic Relative Strength Index

        NOTE: The STOCHRSI function has an unstable period.
        :param timeperiod:
        :param fastk_period:
        :param fastd_period:
        :param fastd_matype:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            fastk, fastd = talib.STOCHRSI(close, timeperiod=timeperiod, fastk_period=fastk_period,
                                          fastd_period=fastd_period, fastd_matype=fastd_matype)
            return fastk, fastd
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def TRIX(self, timeperiod=30):
        """
        1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
        :param timeperiod:
        :return:
        """
        try:
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.TRIX(close, timeperiod=timeperiod)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def ULTOSC(self, timeperiod1=7, timeperiod2=14, timeperiod3=28):
        """
        Ultimate Oscillator
        :param timeperiod1:
        :param timeperiod2:
        :param timeperiod3:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.ULTOSC(high, low, close, timeperiod1=timeperiod1, timeperiod2=timeperiod2, timeperiod3=timeperiod3)
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def WILLR(self, timeperiod=14):
        """
        Williams' %R
        :param timeperiod:
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.WILLR(high, low, close, timeperiod=14)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)
# ========== TECH MOMENTUM INDICATORS **END** ==========


# ========== PRICE TRANSFORM FUNCTIONS **START** ==========
    def AVGPRICE(self):
        """
        Average Price
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.AVGPRICE(opn, high, low, close)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def MEDPRICE(self):
        """
        Median Price
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            real = talib.MEDPRICE(high, low)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def TYPPRICE(self):
        """
        Typical Price
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.TYPPRICE(high, low, close)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def WCLPRICE(self):
        """
        Weighted Close Price
        :return:
        """
        try:
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            real = talib.WCLPRICE(high, low, close)
            return real
        except Exception as e:
            raise e.with_traceback(e.__traceback__)
# ========== PRICE TRANSFORM FUNCTIONS **END** ==========


# ========== PATTERN RECOGNITION FUNCTIONS **START** ==========
    def CDL2CROWS(self):
        """
        Two Crows
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDL2CROWS(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDL3BLACKCROWS(self):
        """
        Three Black Crows
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDL3BLACKCROWS(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDL3INSIDE(self):
        """
        Three Inside Up/Down
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDL3INSIDE(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDL3LINESTRIKE(self):
        """
        Three-Line Strike
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDL3LINESTRIKE(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDL3OUTSIDE(self):
        """
        Three Outside Up/Down
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDL3OUTSIDE(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDL3STARSINSOUTH(self):
        """
        Three Stars In The South
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDL3STARSINSOUTH(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDL3WHITESOLDIERS(self):
        """
        Three Advancing White Soldiers
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDL3WHITESOLDIERS(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLABANDONEDBABY(self, penetration=0):
        """
        Abandoned Baby
        :param penetration:
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLABANDONEDBABY(opn, high, low, close, penetration=penetration)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLADVANCEBLOCK(self):
        """
        Advance Block
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLADVANCEBLOCK(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLBELTHOLD(self):
        """
        Belt-hold
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLBELTHOLD(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLBREAKAWAY(self):
        """
        Breakaway
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLBREAKAWAY(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLCLOSINGMARUBOZU(self):
        """
        Closing Marubozu
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLCLOSINGMARUBOZU(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLCONCEALBABYSWALL(self):
        """
        Concealing Baby Swallow
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLCONCEALBABYSWALL(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLCOUNTERATTACK(self):
        """
        Counterattack
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLCOUNTERATTACK(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLDARKCLOUDCOVER(self, penetration=0):
        """
        Dark Cloud Cover
        :param penetration:
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLDARKCLOUDCOVER(opn, high, low, close, penetration=penetration)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLDOJI(self):
        """
        Doji
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLDOJI(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLDOJISTAR(self):
        """
        Doji Star
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLDOJISTAR(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLDRAGONFLYDOJI(self):
        """
        Dragonfly Doji
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLDRAGONFLYDOJI(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLENGULFING(self):
        """
        Engulfing Pattern
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLENGULFING(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLEVENINGDOJISTAR(self, penetration=0):
        """
        Evening Doji Star
        :param penetration:
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLEVENINGDOJISTAR(opn, high, low, close, penetration=penetration)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLEVENINGSTAR(self, penetration=0):
        """
        Evening Star
        :param penetration:
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLEVENINGSTAR(opn, high, low, close, penetration=penetration)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLGAPSIDESIDEWHITE(self):
        """
        Up/Down-gap side-by-side white lines
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLGAPSIDESIDEWHITE(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLGRAVESTONEDOJI(self):
        """
        Gravestone Doji
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLGRAVESTONEDOJI(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLHAMMER(self):
        """
        Hammer
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLHAMMER(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLHANGINGMAN(self):
        """
        Hanging Man
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLHANGINGMAN(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLHARAMI(self):
        """
        Harami Pattern
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLHARAMI(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLHARAMICROSS(self):
        """
        Harami Cross Pattern
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLHARAMICROSS(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLHIGHWAVE(self):
        """
        High-Wave Candle
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLHIGHWAVE(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLHIKKAKE(self):
        """
        Hikkake Pattern
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLHIKKAKE(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLHIKKAKEMOD(self):
        """
        Modified Hikkake Pattern
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLHIKKAKEMOD(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLHOMINGPIGEON(self):
        """
        Homing Pigeon
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLHOMINGPIGEON(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLIDENTICAL3CROWS(self):
        """
        Identical Three Crows
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLIDENTICAL3CROWS(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLINNECK(self):
        """
        In-Neck Pattern
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLINNECK(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLINVERTEDHAMMER(self):
        """
        Inverted Hammer
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLINVERTEDHAMMER(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLKICKING(self):
        """
        Kicking
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLKICKING(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLKICKINGBYLENGTH(self):
        """
        Kicking - bull/bear determined by the longer marubozu
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLKICKINGBYLENGTH(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLLADDERBOTTOM(self):
        """
        Ladder Bottom
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLLADDERBOTTOM(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLLONGLEGGEDDOJI(self):
        """
        Long Legged Doji
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLLONGLEGGEDDOJI(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLLONGLINE(self):
        """
        Long Line Candle
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLLONGLINE(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLMARUBOZU(self):
        """
        Marubozu
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLMARUBOZU(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLMATCHINGLOW(self):
        """
        Matching Low
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLMATCHINGLOW(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLMATHOLD(self, penetration=0):
        """
        Mat Hold
        :param penetration:
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLMATHOLD(opn, high, low, close, penetration=penetration)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLMORNINGDOJISTAR(self, penetration=0):
        """
        Morning Doji Star
        :param penetration:
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLMORNINGDOJISTAR(opn, high, low, close, penetration=penetration)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLMORNINGSTAR(self, penetration=0):
        """
        Morning Star
        :param penetration:
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLMORNINGSTAR(opn, high, low, close, penetration=penetration)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLONNECK(self):
        """
        On-Neck Pattern
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLONNECK(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLPIERCING(self):
        """
        Piercing Pattern
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLPIERCING(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLRICKSHAWMAN(self):
        """
        Rickshaw Man
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLRICKSHAWMAN(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLRISEFALL3METHODS(self):
        """
        Rising/Falling Three Methods
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLRISEFALL3METHODS(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLSEPARATINGLINES(self):
        """
        Separating Lines
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLSEPARATINGLINES(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLSHOOTINGSTAR(self):
        """
        Shooting Star
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLSHOOTINGSTAR(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLSHORTLINE(self):
        """
        Short Line Candle
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLSHORTLINE(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLSPINNINGTOP(self):
        """
        Spinning Top
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLSPINNINGTOP(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLSTALLEDPATTERN(self):
        """
        Stalled Pattern
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLSTALLEDPATTERN(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLSTICKSANDWICH(self):
        """
        Stick Sandwich
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLSTICKSANDWICH(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLTAKURI(self):
        """
        Takuri (Dragonfly Doji with very long lower shadow)
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLTAKURI(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLTASUKIGAP(self):
        """
        Tasuki Gap
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLTASUKIGAP(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLTHRUSTING(self):
        """
        Thrusting Pattern
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLTHRUSTING(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLTRISTAR(self):
        """
        Tristar Pattern
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLTRISTAR(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLUNIQUE3RIVER(self):
        """
        Unique 3 River
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLUNIQUE3RIVER(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLUPSIDEGAP2CROWS(self):
        """
        Upside Gap Two Crows
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLUPSIDEGAP2CROWS(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def CDLXSIDEGAP3METHODS(self):
        """
        Upside/Downside Gap Three Methods
        :return:
        """
        try:
            opn = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('opn')], dtype='f8')
            high = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('high')], dtype='f8')
            low = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('low')], dtype='f8')
            close = np.array(self.hp1d[:, Data.DB.Table.EquityHP1d_flds.index('close')], dtype='f8')
            integer = talib.CDLXSIDEGAP3METHODS(opn, high, low, close)
            return integer
        except Exception as e:
            raise e.with_traceback(e.__traceback__)
# ========== PATTERN RECOGNITION FUNCTIONS **END** ==========

if __name__ == '__main__':
    aapl = Equity('AAPL', 'Apple, Inc.')
    aapl.get_hp1d()
    # print(aapl.hp1d)
    print(aapl.BBANDS())
    print(aapl.DEMA())
    print(aapl.EMA())
    print(aapl.CDLCOUNTERATTACK())