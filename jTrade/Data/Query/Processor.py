
import json
import datetime

import Data.Query.Query

class Quote(object):
    def __init__(self, symbols : list):
        try:
            self.obj_dict = {}

            response = Data.Query.Query.EQUITY(symbols)
            time = datetime.datetime.strptime(response['query']['created'], '%Y-%m-%dT%H:%M:%SZ')
            for quote in response['query']['results']['quote']:
                    self.obj_dict[(quote['Symbol'], time)] = {
                    'symbol': quote['Symbol'],
                    'time': time,
                    'price': float(quote['LastTradePriceOnly']),
                    'change': float(quote['Change']),
                    'volume': float(quote['Volume']),
                    'avg_volume': float(quote['AverageDailyVolume']),
                    'name': quote['Name'],
                    'exchange': quote['StockExchange'],
                    'market_cap': float(quote['MarketCapitalization'][:-1]) if quote['MarketCapitalization'][-1] == 'B' \
                        else float(quote['MarketCapitalization'][:-1]) / 1000 if quote['MarketCapitalization'][
                                                                                     -1] == 'M' \
                        else float(quote['MarketCapitalization'][:-1]) / 1e6,
                    'day_high': float(quote['DaysHigh']),
                    'day_low': float(quote['DaysLow']),
                    'year_high': float(quote['YearHigh']),
                    'year_low': float(quote['YearLow'])
                }
        except Exception as e:
            raise e.with_traceback(e.__traceback__)
