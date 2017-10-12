import talib
import numpy as np

import jTrade.Core.Instrument.Equity as Equity


# ========== TECH OVERLAP INDICATORS **START** ==========

def BBANDS(equity, start=None, end=None, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0):
    """Bollinger Bands

    :param timeperiod:
    :param nbdevup:
    :param nbdevdn:
    :param matype:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    upperband, middleband, lowerband = talib.BBANDS(close, timeperiod=timeperiod, nbdevup=nbdevup, nbdevdn=nbdevdn, matype=matype)
    return upperband, middleband, lowerband


def DEMA(equity, start=None, end=None, timeperiod=30):
    """Double Exponential Moving Average

    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.DEMA(close, timeperiod=timeperiod)
    return real


def EMA(equity, start=None, end=None, timeperiod=30):
    """Exponential Moving Average


    NOTE: The EMA function has an unstable period.
    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.EMA(close, timeperiod=timeperiod)
    return real


def HT_TRENDLINE(equity, start=None, end=None):
    """Hilbert Transform - Instantaneous Trendline


    NOTE: The HT_TRENDLINE function has an unstable period.
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.HT_TRENDLINE(close)
    return real


def KAMA(equity, start=None, end=None, timeperiod=30):
    """Kaufman Adaptive Moving Average


    NOTE: The KAMA function has an unstable period.
    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.KAMA(close, timeperiod=timeperiod)
    return real


def MA(equity, start=None, end=None, timeperiod=30, matype=0):
    """Moving average

    :param timeperiod:
    :param matype:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.MA(close, timeperiod=timeperiod, matype=matype)
    return real


def MAMA(equity, start=None, end=None, fastlimit=0, slowlimit=0):
    """MESA Adaptive Moving Average


    NOTE: The MAMA function has an unstable period.
    :param fastlimit:
    :param slowlimit:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    mama, fama = talib.MAMA(close, fastlimit=fastlimit, slowlimit=slowlimit)
    return mama, fama


def MAVP(equity, periods, start=None, end=None, minperiod=2, maxperiod=30, matype=0):
    """Moving average with variable period

    :param periods:
    :param minperiod:
    :param maxperiod:
    :param matype:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.MAVP(close, periods, minperiod=minperiod, maxperiod=maxperiod, matype=matype)
    return real


def MIDPOINT(equity, start=None, end=None, timeperiod=14):
    """MidPoint over period

    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.MIDPOINT(close, timeperiod=timeperiod)
    return real


def MIDPRICE(equity, start=None, end=None, timeperiod=14):
    """Midpoint Price over period

    :param timeperiod:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    real = talib.MIDPRICE(high, low, timeperiod=timeperiod)
    return real


def SAR(equity, start=None, end=None, acceleration=0, maximum=0):
    """Parabolic SAR

    :param acceleration:
    :param maximum:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    real = talib.SAR(high, low, acceleration=acceleration, maximum=maximum)
    return real


def SAREXT(equity, start=None, end=None, startvalue=0, offsetonreverse=0, accelerationinitlong=0, accelerationlong=0,
       accelerationmaxlong=0, accelerationinitshort=0, accelerationshort=0, accelerationmaxshort=0):
    """Parabolic SAR - Extended

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
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    real = talib.SAREXT(high, low, startvalue=startvalue, offsetonreverse=offsetonreverse, accelerationinitlong=accelerationinitlong,
                        accelerationlong=accelerationlong, accelerationmaxlong=accelerationmaxlong, accelerationinitshort=accelerationinitshort,
                        accelerationshort=accelerationshort, accelerationmaxshort=accelerationmaxshort)
    return real


def SMA(equity, start=None, end=None, timeperiod=30):
    """Simple Moving Average

    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.SMA(close, timeperiod=timeperiod)
    return real


def T3(equity, start=None, end=None, timeperiod=5, vfactor=0):
    """Triple Exponential Moving Average (T3)


    NOTE: The T3 function has an unstable period.
    :param timeperiod:
    :param vfactor:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.T3(close, timeperiod=timeperiod, vfactor=vfactor)
    return real


def TEMA(equity, start=None, end=None, timeperiod=30):
    """Triple Exponential Moving Average

    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.TEMA(close, timeperiod=timeperiod)
    return real


def TRIMA(equity, start=None, end=None, timeperiod=30):
    """Triangular Moving Average

    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.TRIMA(close, timeperiod=timeperiod)
    return real


def WMA(equity, start=None, end=None, timeperiod=30):
    """Weighted Moving Average

    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.WMA(close, timeperiod=timeperiod)
    return real
# ========== TECH OVERLAP INDICATORS **END** ==========


# ========== TECH MOMENTUM INDICATORS **START** ==========

def ADX(equity, start=None, end=None, timeperiod=14):
    """Average Directional Movement Index


    NOTE: The ADX function has an unstable period.
    :param timeperiod:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.ADX(high, low, close, timeperiod=timeperiod)
    return real


def ADXR(equity, start=None, end=None, timeperiod=14):
    """Average Directional Movement Index Rating


    NOTE: The ADXR function has an unstable period.
    :param timeperiod:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.ADXR(high, low, close, timeperiod=timeperiod)
    return real


def APO(equity, start=None, end=None, fastperiod=12, slowperiod=26, matype=0):
    """Absolute Price Oscillator

    :param fastperiod:
    :param slowperiod:
    :param matype:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.APO(close, fastperiod=fastperiod, slowperiod=slowperiod, matype=matype)
    return real


def AROON(equity, start=None, end=None, timeperiod=14):
    """Aroon

    :param timeperiod:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    aroondown, aroonup = talib.AROON(high, low, timeperiod=timeperiod)
    return aroondown, aroonup


def AROONOSC(equity, start=None, end=None, timeperiod=14):
    """Aroon Oscillator

    :param timeperiod:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    real = talib.AROONOSC(high, low, timeperiod=timeperiod)
    return real


def BOP(equity, start=None, end=None):
    """Balance Of Power

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.BOP(opn, high, low, close)
    return real


def CCI(equity, start=None, end=None, timeperiod=14):
    """Commodity Channel Index

    :param timeperiod:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.CCI(high, low, close, timeperiod=timeperiod)
    return real


def CMO(equity, start=None, end=None, timeperiod=14):
    """Chande Momentum Oscillator

    NOTE: The CMO function has an unstable period.
    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.CMO(close, timeperiod=timeperiod)
    return real


def DX(equity, start=None, end=None, timeperiod=14):
    """Directional Movement Index


    NOTE: The DX function has an unstable period.
    :param timeperiod:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.DX(high, low, close, timeperiod=timeperiod)
    return real


def MACD(equity, start=None, end=None, fastperiod=12, slowperiod=26, signalperiod=9):
    """Moving Average Convergence/Divergence

    :param fastperiod:
    :param slowperiod:
    :param signalperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    macd, macdsignal, macdhist = talib.MACD(close, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)
    return macd, macdsignal, macdhist


def MACDEXT(equity, start=None, end=None, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0):
    """MACD with controllable MA type

    :param fastperiod:
    :param fastmatype:
    :param slowperiod:
    :param slowmatype:
    :param signalperiod:
    :param signalmatype:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    macd, macdsignal, macdhist = talib.MACDEXT(close, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0,
                                               signalperiod=9, signalmatype=0)
    return macd, macdsignal, macdhist


def MACDFIX(equity, start=None, end=None, signalperiod=9):
    """Moving Average Convergence/Divergence Fix 12/26

    :param signalperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    macd, macdsignal, macdhist = talib.MACDFIX(close, signalperiod=signalperiod)
    return macd, macdsignal, macdhist


def MFI(equity, start=None, end=None, timeperiod=14):
    """Money Flow Index


    NOTE: The MFI function has an unstable period.
    :param timeperiod:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    volume = np.array(equity.hp.loc[start:end, 'volume'], dtype='f8')
    real = talib.MFI(high, low, close, volume, timeperiod=timeperiod)
    return real


def MINUS_DI(equity, start=None, end=None, timeperiod=14):
    """Minus Directional Signal


    NOTE: The MINUS_DI function has an unstable period.
    :param timeperiod:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.MINUS_DI(high, low, close, timeperiod=timeperiod)
    return real


def MINUS_DM(equity, start=None, end=None, timeperiod=14):
    """Minus Directional Movement


    NOTE: The MINUS_DM function has an unstable period.
    :param timeperiod:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    real = talib.MINUS_DM(high, low, timeperiod=timeperiod)
    return real


def MOM(equity, start=None, end=None, timeperiod=10):
    """Momentum

    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.MOM(close, timeperiod=timeperiod)
    return real


def PLUS_DI(equity, start=None, end=None, timeperiod=14):
    """Plus Directional Signal


    NOTE: The PLUS_DI function has an unstable period.
    :param timeperiod:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.PLUS_DI(high, low, close, timeperiod=timeperiod)
    return real


def PLUS_DM(equity, start=None, end=None, timeperiod=14):
    """Plus Directional Movement


    NOTE: The PLUS_DM function has an unstable period.
    :param timeperiod:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    real = talib.PLUS_DM(high, low, timeperiod=timeperiod)
    return real


def PPO(equity, start=None, end=None, fastperiod=12, slowperiod=26, matype=0):
    """Percentage Price Oscillator

    :param fastperiod:
    :param slowperiod:
    :param matype:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.PPO(close, fastperiod=fastperiod, slowperiod=slowperiod, matype=matype)
    return real


def ROC(equity, start=None, end=None, timeperiod=10):
    """Rate of change : ((price/prevPrice)-1)*100

    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.ROC(close, timeperiod=timeperiod)
    return real


def ROCP(equity, start=None, end=None, timeperiod=10):
    """Rate of change Percentage: (price-prevPrice)/prevPrice

    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.ROCP(close, timeperiod=timeperiod)
    return real


def ROCR(equity, start=None, end=None, timeperiod=10):
    """Rate of change ratio: (price/prevPrice)

    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.ROCR(close, timeperiod=timeperiod)
    return real


def ROCR100(equity, start=None, end=None, timeperiod=10):
    """Rate of change ratio 100 scale: (price/prevPrice)*100

    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.ROCR100(close, timeperiod=timeperiod)
    return real


def RSI(equity, start=None, end=None, timeperiod=14):
    """Relative Strength Index


    NOTE: The RSI function has an unstable period.
    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.RSI(close, timeperiod=timeperiod)
    return real


def STOCH(equity, start=None, end=None, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0):
    """Stochastic

    :param fastk_period:
    :param slowk_period:
    :param slowk_matype:
    :param slowd_period:
    :param slowd_matype:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    slowk, slowd = talib.STOCH(high, low, close, fastk_period=fastk_period, slowk_period=slowk_period,
                               slowk_matype=slowk_matype, slowd_period=slowd_period, slowd_matype=slowd_matype)
    return slowk, slowd


def STOCHF(equity, start=None, end=None, fastk_period=5, fastd_period=3, fastd_matype=0):
    """Stochastic Fast

    :param fastk_period:
    :param fastd_period:
    :param fastd_matype:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    fastk, fastd = talib.STOCHF(high, low, close, fastk_period=fastk_period, fastd_period=fastd_period,
                                fastd_matype=fastd_matype)
    return fastk, fastd


def STOCHRSI(equity, start=None, end=None, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0):
    """Stochastic Relative Strength Index


    NOTE: The STOCHRSI function has an unstable period.
    :param timeperiod:
    :param fastk_period:
    :param fastd_period:
    :param fastd_matype:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    fastk, fastd = talib.STOCHRSI(close, timeperiod=timeperiod, fastk_period=fastk_period,
                                  fastd_period=fastd_period, fastd_matype=fastd_matype)
    return fastk, fastd


def TRIX(equity, start=None, end=None, timeperiod=30):
    """1-day Rate-Of-Change (ROC) of a Triple Smooth EMA

    :param timeperiod:
    :return:
    """
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.TRIX(close, timeperiod=timeperiod)
    return real


def ULTOSC(equity, start=None, end=None, timeperiod1=7, timeperiod2=14, timeperiod3=28):
    """Ultimate Oscillator

    :param timeperiod1:
    :param timeperiod2:
    :param timeperiod3:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.ULTOSC(high, low, close, timeperiod1=timeperiod1, timeperiod2=timeperiod2, timeperiod3=timeperiod3)


def WILLR(equity, start=None, end=None, timeperiod=14):
    """Williams' %R

    :param timeperiod:
    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.WILLR(high, low, close, timeperiod=14)
    return real
# ========== TECH MOMENTUM INDICATORS **END** ==========


# ========== PRICE TRANSFORM FUNCTIONS **START** ==========

def AVGPRICE(equity, start=None, end=None):
    """Average Price

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.AVGPRICE(opn, high, low, close)
    return real


def MEDPRICE(equity, start=None, end=None):
    """Median Price

    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    real = talib.MEDPRICE(high, low)
    return real


def TYPPRICE(equity, start=None, end=None):
    """Typical Price

    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.TYPPRICE(high, low, close)
    return real


def WCLPRICE(equity, start=None, end=None):
    """Weighted Close Price

    :return:
    """
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    real = talib.WCLPRICE(high, low, close)
    return real
# ========== PRICE TRANSFORM FUNCTIONS **END** ==========


# ========== PATTERN RECOGNITION FUNCTIONS **START** ==========

def CDL2CROWS(equity, start=None, end=None):
    """Two Crows

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDL2CROWS(opn, high, low, close)
    return integer


def CDL3BLACKCROWS(equity, start=None, end=None):
    """Three Black Crows

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDL3BLACKCROWS(opn, high, low, close)
    return integer


def CDL3INSIDE(equity, start=None, end=None):
    """Three Inside Up/Down

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDL3INSIDE(opn, high, low, close)
    return integer


def CDL3LINESTRIKE(equity, start=None, end=None):
    """Three-Line Strike

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDL3LINESTRIKE(opn, high, low, close)
    return integer


def CDL3OUTSIDE(equity, start=None, end=None):
    """Three Outside Up/Down

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDL3OUTSIDE(opn, high, low, close)
    return integer


def CDL3STARSINSOUTH(equity, start=None, end=None):
    """Three Stars In The South

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDL3STARSINSOUTH(opn, high, low, close)
    return integer


def CDL3WHITESOLDIERS(equity, start=None, end=None):
    """Three Advancing White Soldiers

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDL3WHITESOLDIERS(opn, high, low, close)
    return integer


def CDLABANDONEDBABY(equity, start=None, end=None, penetration=0):
    """Abandoned Baby

    :param penetration:
    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLABANDONEDBABY(opn, high, low, close, penetration=penetration)
    return integer


def CDLADVANCEBLOCK(equity, start=None, end=None):
    """Advance Block

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLADVANCEBLOCK(opn, high, low, close)
    return integer


def CDLBELTHOLD(equity, start=None, end=None):
    """Belt-hold

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLBELTHOLD(opn, high, low, close)
    return integer


def CDLBREAKAWAY(equity, start=None, end=None):
    """Breakaway

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLBREAKAWAY(opn, high, low, close)
    return integer


def CDLCLOSINGMARUBOZU(equity, start=None, end=None):
    """Closing Marubozu

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLCLOSINGMARUBOZU(opn, high, low, close)
    return integer


def CDLCONCEALBABYSWALL(equity, start=None, end=None):
    """Concealing Baby Swallow

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLCONCEALBABYSWALL(opn, high, low, close)
    return integer


def CDLCOUNTERATTACK(equity, start=None, end=None):
    """Counterattack

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLCOUNTERATTACK(opn, high, low, close)
    return integer


def CDLDARKCLOUDCOVER(equity, start=None, end=None, penetration=0):
    """Dark Cloud Cover

    :param penetration:
    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLDARKCLOUDCOVER(opn, high, low, close, penetration=penetration)
    return integer


def CDLDOJI(equity, start=None, end=None):
    """Doji

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLDOJI(opn, high, low, close)
    return integer


def CDLDOJISTAR(equity, start=None, end=None):
    """Doji Star

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLDOJISTAR(opn, high, low, close)
    return integer


def CDLDRAGONFLYDOJI(equity, start=None, end=None):
    """Dragonfly Doji

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLDRAGONFLYDOJI(opn, high, low, close)
    return integer


def CDLENGULFING(equity, start=None, end=None):
    """Engulfing Pattern

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLENGULFING(opn, high, low, close)
    return integer


def CDLEVENINGDOJISTAR(equity, start=None, end=None, penetration=0):
    """Evening Doji Star

    :param penetration:
    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLEVENINGDOJISTAR(opn, high, low, close, penetration=penetration)
    return integer


def CDLEVENINGSTAR(equity, start=None, end=None, penetration=0):
    """Evening Star

    :param penetration:
    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLEVENINGSTAR(opn, high, low, close, penetration=penetration)
    return integer


def CDLGAPSIDESIDEWHITE(equity, start=None, end=None):
    """Up/Down-gap side-by-side white lines

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLGAPSIDESIDEWHITE(opn, high, low, close)
    return integer


def CDLGRAVESTONEDOJI(equity, start=None, end=None):
    """Gravestone Doji

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLGRAVESTONEDOJI(opn, high, low, close)
    return integer


def CDLHAMMER(equity, start=None, end=None):
    """Hammer

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLHAMMER(opn, high, low, close)
    return integer


def CDLHANGINGMAN(equity, start=None, end=None):
    """Hanging Man

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLHANGINGMAN(opn, high, low, close)
    return integer


def CDLHARAMI(equity, start=None, end=None):
    """Harami Pattern

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLHARAMI(opn, high, low, close)
    return integer


def CDLHARAMICROSS(equity, start=None, end=None):
    """Harami Cross Pattern

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLHARAMICROSS(opn, high, low, close)
    return integer


def CDLHIGHWAVE(equity, start=None, end=None):
    """High-Wave Candle

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLHIGHWAVE(opn, high, low, close)
    return integer


def CDLHIKKAKE(equity, start=None, end=None):
    """Hikkake Pattern

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLHIKKAKE(opn, high, low, close)
    return integer


def CDLHIKKAKEMOD(equity, start=None, end=None):
    """Modified Hikkake Pattern

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLHIKKAKEMOD(opn, high, low, close)
    return integer


def CDLHOMINGPIGEON(equity, start=None, end=None):
    """Homing Pigeon

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLHOMINGPIGEON(opn, high, low, close)
    return integer


def CDLIDENTICAL3CROWS(equity, start=None, end=None):
    """Identical Three Crows

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLIDENTICAL3CROWS(opn, high, low, close)
    return integer


def CDLINNECK(equity, start=None, end=None):
    """In-Neck Pattern

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLINNECK(opn, high, low, close)
    return integer


def CDLINVERTEDHAMMER(equity, start=None, end=None):
    """Inverted Hammer

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLINVERTEDHAMMER(opn, high, low, close)
    return integer


def CDLKICKING(equity, start=None, end=None):
    """Kicking

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLKICKING(opn, high, low, close)
    return integer


def CDLKICKINGBYLENGTH(equity, start=None, end=None):
    """Kicking - bull/bear determined by the longer marubozu

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLKICKINGBYLENGTH(opn, high, low, close)
    return integer


def CDLLADDERBOTTOM(equity, start=None, end=None):
    """Ladder Bottom

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLLADDERBOTTOM(opn, high, low, close)
    return integer


def CDLLONGLEGGEDDOJI(equity, start=None, end=None):
    """Long Legged Doji

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLLONGLEGGEDDOJI(opn, high, low, close)
    return integer


def CDLLONGLINE(equity, start=None, end=None):
    """Long Line Candle

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLLONGLINE(opn, high, low, close)
    return integer


def CDLMARUBOZU(equity, start=None, end=None):
    """Marubozu

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLMARUBOZU(opn, high, low, close)
    return integer


def CDLMATCHINGLOW(equity, start=None, end=None):
    """Matching Low

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLMATCHINGLOW(opn, high, low, close)
    return integer


def CDLMATHOLD(equity, start=None, end=None, penetration=0):
    """Mat Hold

    :param penetration:
    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLMATHOLD(opn, high, low, close, penetration=penetration)
    return integer


def CDLMORNINGDOJISTAR(equity, start=None, end=None, penetration=0):
    """Morning Doji Star

    :param penetration:
    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLMORNINGDOJISTAR(opn, high, low, close, penetration=penetration)
    return integer


def CDLMORNINGSTAR(equity, start=None, end=None, penetration=0):
    """Morning Star

    :param penetration:
    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLMORNINGSTAR(opn, high, low, close, penetration=penetration)
    return integer


def CDLONNECK(equity, start=None, end=None):
    """On-Neck Pattern

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLONNECK(opn, high, low, close)
    return integer


def CDLPIERCING(equity, start=None, end=None):
    """Piercing Pattern

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLPIERCING(opn, high, low, close)
    return integer


def CDLRICKSHAWMAN(equity, start=None, end=None):
    """Rickshaw Man

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLRICKSHAWMAN(opn, high, low, close)
    return integer


def CDLRISEFALL3METHODS(equity, start=None, end=None):
    """Rising/Falling Three Methods

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLRISEFALL3METHODS(opn, high, low, close)
    return integer


def CDLSEPARATINGLINES(equity, start=None, end=None):
    """Separating Lines

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLSEPARATINGLINES(opn, high, low, close)
    return integer


def CDLSHOOTINGSTAR(equity, start=None, end=None):
    """Shooting Star

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLSHOOTINGSTAR(opn, high, low, close)
    return integer


def CDLSHORTLINE(equity, start=None, end=None):
    """Short Line Candle

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLSHORTLINE(opn, high, low, close)
    return integer


def CDLSPINNINGTOP(equity, start=None, end=None):
    """Spinning Top

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLSPINNINGTOP(opn, high, low, close)
    return integer


def CDLSTALLEDPATTERN(equity, start=None, end=None):
    """Stalled Pattern

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLSTALLEDPATTERN(opn, high, low, close)
    return integer


def CDLSTICKSANDWICH(equity, start=None, end=None):
    """Stick Sandwich

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLSTICKSANDWICH(opn, high, low, close)
    return integer


def CDLTAKURI(equity, start=None, end=None):
    """Takuri (Dragonfly Doji with very long lower shadow)

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLTAKURI(opn, high, low, close)
    return integer


def CDLTASUKIGAP(equity, start=None, end=None):
    """Tasuki Gap

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLTASUKIGAP(opn, high, low, close)
    return integer


def CDLTHRUSTING(equity, start=None, end=None):
    """Thrusting Pattern

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLTHRUSTING(opn, high, low, close)
    return integer


def CDLTRISTAR(equity, start=None, end=None):
    """Tristar Pattern

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLTRISTAR(opn, high, low, close)
    return integer


def CDLUNIQUE3RIVER(equity, start=None, end=None):
    """Unique 3 River

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLUNIQUE3RIVER(opn, high, low, close)
    return integer


def CDLUPSIDEGAP2CROWS(equity, start=None, end=None):
    """Upside Gap Two Crows

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLUPSIDEGAP2CROWS(opn, high, low, close)
    return integer


def CDLXSIDEGAP3METHODS(equity, start=None, end=None):
    """Upside/Downside Gap Three Methods

    :return:
    """
    opn = np.array(equity.hp.loc[start:end, 'open'], dtype='f8')
    high = np.array(equity.hp.loc[start:end, 'high'], dtype='f8')
    low = np.array(equity.hp.loc[start:end, 'low'], dtype='f8')
    close = np.array(equity.hp.loc[start:end, 'close'], dtype='f8')
    integer = talib.CDLXSIDEGAP3METHODS(opn, high, low, close)
    return integer
# ========== PATTERN RECOGNITION FUNCTIONS **END** ==========

if __name__ == '__main__':
    import datetime
    today = datetime.date(2017,8,30)

    eq = Equity.Equity('AAPL')
    eq.get_hp()
    print((CDLSPINNINGTOP(eq)))
    print('ok')