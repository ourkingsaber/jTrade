import base64
import json
import urllib.parse
import urllib.request
import quandl
import datetime
import pandas as pd
# from rpy2.robjects import packages as rpackages, pandas2ri, r

import jtrade.util.Credential as Credential
import jtrade.data.table as Table
from jtrade.util.exception import *
from jtrade.data.db_manager import dbmanager

quandl.ApiConfig.api_key = Credential.quandl['apikey']


class Intrinio(object):
    """Fetch data from Intrinio"""

    @staticmethod
    def EquityFin(symbol, year, period, statement):
        response = Intrinio._EquityFin_query(symbol, year, period, statement)
        if not response['data']:
            raise NoDataError('No data on Intrinio for input: {}, {}, {}, {}'.format(symbol, year, period, statement))
        resdict = {item['tag']: [item['value'] if isinstance(item['value'], float) else None] for item in response['data']}
        resdict['symbol'] = symbol
        resdict['year'] = year
        resdict['period'] = period
        df = pd.DataFrame(resdict)
        return df

    @staticmethod
    def _EquityFin_query(symbol, year, period, statement):
        if statement not in ('income_statement', 'balance_sheet', 'cash_flow_statement', 'calculations'):
            raise ValueError('{} is not a valid statement'.format(statement))
        if period not in ('FY','Q1','Q2','Q3','Q4','Q1TTM','Q2TTM','Q3TTM','Q2YTD','Q3YTD'):
            raise ValueError('{} is not a period'.format(period))
        req = urllib.request.Request(
            'https://api.intrinio.com/financials/standardized?identifier={}&statement={}&fiscal_year={}&fiscal_period={}'.format(
            symbol, statement, year, period))
        req.add_header('Authorization', b'Basic ' + base64.b64encode(Credential.intrino['user'] + b':' + Credential.intrino['pw']))
        result = urllib.request.urlopen(req).read()
        if isinstance(result, bytes):
            result = result.decode('utf-8')
        return json.loads(result)

    @staticmethod
    def stmt_to_table(statement):
        if statement == 'income_statement':
            return Table.EquityFinIS
        elif statement == 'balance_sheet':
            return Table.EquityFinBS
        elif statement == 'cash_flow_statement':
            return Table.EquityFinCF
        elif statement == 'calculations':
            return Table.EquityFinFund
        else:
            raise ValueError('{} is not a valid statement'.format(statement))

    @staticmethod
    def is_duplicate(symbol, year, period, statement):
        """Checks duplicate to reduce number of queries (Intrino has daily limit)"""
        fltr = {'&': {
            ('symbol', '='): symbol,
            ('year', '='): year,
            ('period', '='): period
        }}
        df = dbmanager.select(Intrinio.stmt_to_table(statement), fltr, parse_dates=False)
        return df.shape[0] > 0


class Quandl(object):
    """Fetch data from Quandl"""

    @staticmethod
    def EquityHP(symbols, start, end):
        if isinstance(symbols, str):
            symbols = [symbols]
        symbolstr = ','.join(symbols)
        datestr = ','.join(d.isoformat() for d in (start + datetime.timedelta(x) for x in range((end-start).days + 1)))
        df = quandl.get_table('WIKI/PRICES', ticker=symbolstr, date=datestr)
        df.rename(columns={'ticker': 'symbol', 'ex-dividend': 'ex_dividend'}, inplace=True)
        return df


class Yahoo(object):
    """Fetches data from Yahoo."""

    @staticmethod
    def EquityQuote(symbols : list):
        response = Yahoo._EquityQuote_query(symbols)
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

    @staticmethod
    def EquityHP(symbol, length):
        response = Yahoo._EquityHP_query(symbol, length)
        timestamp = response['chart']['result'][0]['timestamp']
        gmt_offset = int(response['chart']['result'][0]['meta']['gmtoffset']) // 3600
        indicator = response['chart']['result'][0]['indicators']
        res_lst = []
        for i in range(len(timestamp)):
            date = datetime.datetime.fromtimestamp(timestamp[i], datetime.timezone(datetime.timedelta(hours=-gmt_offset))).date()
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

    @staticmethod
    def _EquityQuote_query(symbols : list):
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        ticker_url = "','".join(symbols)
        yql_query = "select * from yahoo.finance.quotes where symbol in ('{}')".format(ticker_url)
        yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + \
                  "&format=json&diagnostics=true&env=store://data.Tables.org/alltableswithkeys&callback="
        print(yql_url)
        result = urllib.request.urlopen(yql_url).read()
        if isinstance(result, bytes):
            result = result.decode('utf-8')
        return json.loads(result)

    @staticmethod
    def _EquityHP_query(symbol, length):
        if length not in ["1d","5d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"]:
            raise ValueError('Time range not valid.')

        url = 'https://query1.finance.yahoo.com/v7/finance/chart/{}?range={}&interval=1d&indicators=quote&includeTimestamps=true'.format(symbol, length)

        result = urllib.request.urlopen(url).read()
        if isinstance(result, bytes):
            result = result.decode('utf-8')
        return json.loads(result)



# class QuantMod(object):
#     """Fetches data using quantmod, an R package."""
#
#     quantmod = rpackages.importr('quantmod')
#     pandas2ri.activate()
#
#     @staticmethod
#     def EquityHP(symbol, start, end):
#         # gets a ndarray
#         r('{} = getSymbols("{}",from="{}",to="{}",src="google",auto.assign=F)'.format(
#             symbol+'.hp', symbol, start.isoformat(), end.isoformat()))
#         # convert to dataframe
#         r('{} = data.frame(date=index({}), coredata({}))'.format(symbol+'.hp', symbol+'.hp', symbol+'.hp'))
#         hps = pd.DataFrame(r[symbol+'.hp'])
#         # convert days since epoch to datetime
#         epoch = datetime.date(1970, 1, 1)
#         hps.loc[:,'date'] = [epoch+datetime.timedelta(days=int(d)) for d in hps.loc[:,'date']]
#         # add column of symbol
#         hps['symbol'] = symbol
#         # convert column names
#         hps.columns = [name.split('.')[-1].lower() for name in hps.columns]
#         return hps


if __name__ == '__main__':
    # print(Yahoo._EquityQuote_query(['AAPL', 'MSFT']))
    # print(Yahoo._EquityHP_query('AAPL', '1y'))
    # print(Yahoo.EquityHP('AAPL', '1y'))

    # print(Intrino._EquityFin_query('DDD', 2000, 'Q1', 'cash_flow_statement'))
    print(Intrinio.EquityFin('FB', 2010, 'Q1', 'balance_sheet'))


    sym = 'AAPL'
    periods = ('FY', 'Q1', 'Q2', 'Q3', 'Q4')

    # s = ['AAPL','FB']
    # hp = Quandl.EquityHP(s, datetime.date(2017, 1, 1), datetime.date(2017, 1, 10))
    # print(hp.shape[0])

    # a = datetime.datetime.now()
    # for i in range(100):
    #     b = Intrino.is_duplicate('AAPL', 2017, 'Q1', 'cash_flow_statement')
    # print(datetime.datetime.now() - a)


