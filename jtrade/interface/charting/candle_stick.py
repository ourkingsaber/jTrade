import datetime

import plotly as py
import plotly.graph_objs as go

from jtrade.data.db_manager import dbmanager
from jtrade.data.table import EquityHP

df = dbmanager.select(EquityHP, {'&': {('symbol','='): 'AAPL', ('date', '>'): datetime.date(2017,1,1)}})
print(df)
trace = go.Candlestick(x=df.index,
                       open=df.open,
                       high=df.high,
                       low=df.low,
                       close=df.close)
data = [trace]
py.offline.plot(data, filename='simple_candlestick')