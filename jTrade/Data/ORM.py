from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Quote(Base):
    __tablename__ = 'Quote'

    symbol = Column(String(collation='utf8'), primary_key=True)
    time = Column(DateTime(), primary_key=True)
    price = Column(Float())
    change = Column(Float())
    volume = Column(Float())
    avg_volume = Column(Float())
    name = Column(String(collation='utf8'))
    exchange = Column(String(collation='utf8'))
    market_cap = Column(Float())
    day_high = Column(Float())
    day_low = Column(Float())
    year_high = Column(Float())
    year_low = Column(Float())

    def __init__(self, symbol, time, price, change, volume, avg_volume, name, exchange, market_cap, day_high, day_low,
                 year_high, year_low):
        try:
            self.symbol = symbol
            self.time = time
            self.price = price
            self.change = change
            self.volume = volume
            self.avg_volume = avg_volume
            self.name = name
            self.exchange = exchange
            self.market_cap = market_cap
            self.day_high = day_high
            self.day_low = day_low
            self.year_high = year_high
            self.year_low = year_low
        except Exception as e:
            raise e.with_traceback(e.__traceback__)