
import json
import datetime
import pandas as pd
import urllib.parse
import urllib.request


class Yahoo(object):

    @staticmethod
    def quote(symbols : list):
        try:
            response = Yahoo._quote_query(symbols)
            time = datetime.datetime.strptime(response['query']['created'], '%Y-%m-%dT%H:%M:%SZ')
            res_lst = []
            for quote in response['query']['results']['quote']:
                res_lst.append({
                    'symbol': quote['Symbol'],
                    'time': time,
                    'price': float(quote['LastTradePriceOnly']),
                    'change': float(quote['Change']),
                    'pct_change': float(quote['PercentChange'][:-1]),
                    'volume': float(quote['Volume']),
                    'avg_volume': float(quote['AverageDailyVolume']),
                    'name': quote['Name'],
                    'exchange': quote['StockExchange'],
                    'market_cap': float(quote['MarketCapitalization'][:-1]) if quote['MarketCapitalization'][-1] == 'B' \
                        else float(quote['MarketCapitalization'][:-1]) / 1000 if quote['MarketCapitalization'][-1] == 'M' \
                        else float(quote['MarketCapitalization'][:-1]) / 1e6,
                    'day_high': float(quote['DaysHigh']),
                    'day_low': float(quote['DaysLow']),
                    'year_high': float(quote['YearHigh']),
                    'year_low': float(quote['YearLow'])
                })
            df = pd.DataFrame(res_lst)
            return df
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    @staticmethod
    def hp1d(symbol, length):
        try:
            response = Yahoo._hp1d_query(symbol, length)
            res_lst = []
            timestamp = response['chart']['result'][0]['timestamp']
            gmt_offset = int(response['chart']['result'][0]['meta']['gmtoffset']) // 3600
            indicator = response['chart']['result'][0]['indicators']
            for i in range(len(timestamp)):
                print(i)
                date = datetime.datetime.fromtimestamp(timestamp[i],
                                                       datetime.timezone(datetime.timedelta(hours=-gmt_offset))).date()
                res_lst.append({
                    'symbol': symbol,
                    'date': date,
                    'open': float(indicator['quote'][0]['open'][i]),
                    'high': float(indicator['quote'][0]['high'][i]),
                    'low': float(indicator['quote'][0]['low'][i]),
                    'close': float(indicator['quote'][0]['close'][i]),
                    'volume': float(indicator['quote'][0]['volume'][i]),
                    'adjusted': float(indicator['adjclose'][0]['adjclose'][i]),
                })
            df = pd.DataFrame(res_lst, index=[hp['date'] for hp in res_lst])
            return df
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    @staticmethod
    def _quote_query(symbols : list):
        try:
            baseurl = "https://query.yahooapis.com/v1/public/yql?"
            ticker_url = "','".join(symbols)
            yql_query = "select * from yahoo.finance.quotes where symbol in ('{}')".format(ticker_url)
            yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + \
                      "&format=json&diagnostics=true&env=store://datatables.org/alltableswithkeys&callback="
            print(yql_url)
            result = urllib.request.urlopen(yql_url).read()
            return json.loads(result)
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    @staticmethod
    def _hp1d_query(symbol, length):
        try:
            if length not in ["1d","5d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"]:
                raise ValueError('Time range not valid.')

            url = 'https://query1.finance.yahoo.com/v7/finance/chart/{}?range={}&interval=1d&indicators=quote&includeTimestamps=true'.format(symbol, length)

            result = urllib.request.urlopen(url).read()
            return json.loads(result)
        except Exception as e:
            raise e.with_traceback(e.__traceback__)



if __name__ == '__main__':
    print(Yahoo._quote_query(['AAPL', 'MSFT']))
    # print(Yahoo._hp1d_query('AAPL', '1y'))
    # print(Yahoo.hp1d('AAPL', '1y'))
