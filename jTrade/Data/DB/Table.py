from sqlalchemy import Table, Column, MetaData, Float, String, Date, DateTime

metadata = MetaData()

EquityHP1d = Table(
    'EquityHP1d', metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('date', Date(), primary_key=True),
    Column('opn', Float()),
    Column('high', Float()),
    Column('low', Float()),
    Column('close', Float()),
    Column('volume', Float())
)
EquityHP1d_flds = list(EquityHP1d.columns.keys())

EquityQuote = Table(
    'EquityQuote', metadata,
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
    'Position', metadata,
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

Trade = Table(
    'Trade', metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('date', Date(), primary_key=True),
    Column('share', Float()),
    Column('price', Float())
)
Trade_flds = list(Trade.columns.keys())
