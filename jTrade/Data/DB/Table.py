from sqlalchemy import Table, Column, MetaData, Float, String, Date, DateTime

_metadata = MetaData()

EquityHP1d = Table(
    'EquityHP1d', _metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('date', Date(), primary_key=True),
    Column('open', Float()),
    Column('high', Float()),
    Column('low', Float()),
    Column('close', Float()),
    Column('volume', Float()),
    Column('adjusted', Float())
)
EquityHP1d_flds = list(EquityHP1d.columns.keys())

EquityQuote = Table(
    'EquityQuote', _metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('time', DateTime(), primary_key=True),
    Column('price', Float()),
    Column('change', Float()),
    Column('pct_change', Float()),
    Column('volume', Float()),
    Column('avg_volume', Float()),
    Column('name', String(collation='utf8')),
    Column('exchange', String(collation='utf8')),
    Column('market_cap', Float()),
    Column('day_high', Float()),
    Column('day_low', Float()),
    Column('year_high', Float()),
    Column('year_low', Float())
)
EquityQuote_flds = list(EquityQuote.columns.keys())

Position = Table(
    'Position', _metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('date', Date(), primary_key=True),
    Column('share', Float()),
    Column('price', Float()),
    Column('value', Float()),
    Column('cost', Float()),
    Column('pct_ret', Float()),
    Column('abs_ret', Float())
)
Position_flds = list(Position.columns.keys())

Order = Table(
    'Order', _metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('date', Date(), primary_key=True),
    Column('share', Float()),
    Column('price', Float()),
    Column('fee', Float()),
    Column('total', Float())
)
Order_flds = list(Order.columns.keys())

EquityInd1d = Table(
    'EquityInd1d', _metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('date', Date(), primary_key=True),
    Column('indicator', String(collation='utf8'), primary_key=True),
    Column('val', Float())
)
EquityInd1d_flds = list(EquityInd1d.columns.keys())