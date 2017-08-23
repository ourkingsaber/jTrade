
import json
import datetime

import urllib.parse
import urllib.request

def YHOO_QUOTE(symbols : list):
    try:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        ticker_url = "','".join(symbols)
        yql_query = "select * from yahoo.finance.quotes where symbol in ('{}')".format(ticker_url)
        yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + \
                  "&format=json&diagnostics=true&env=store://datatables.org/alltableswithkeys&callback="
        result = urllib.request.urlopen(yql_url).read()
        return json.loads(result)
    except Exception as e:
        raise e.with_traceback(e.__traceback__)


def YHOO_HP(symbol, length):
    try:
        if length not in ["1d","5d","1mo","3mo","6mo","1y","2y","5y","10y","ytd","max"]:
            raise ValueError('Time range not valid.')

        url = 'https://query1.finance.yahoo.com/v7/finance/chart/{}?range={}&interval=1d&indicators=quote&includeTimestamps=true'.format(symbol, length)

        result = urllib.request.urlopen(url).read()
        return json.loads(result)
    except Exception as e:
        raise e.with_traceback(e.__traceback__)



if __name__ == '__main__':
    # print(YHOO_QUOTE(['AAPL', 'MSFT']))
    print(YHOO_HP('AAPL', '1y'))