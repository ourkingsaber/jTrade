
import json

import urllib.parse
import urllib.request

def EQUITY(symbols : list):
    try:
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = "select * from yahoo.finance.quote where symbol in ('"
        ticker_url = "','".join(symbols)
        yql_query = yql_query + ticker_url + "')"
        yql_url = baseurl + urllib.parse.urlencode({'q': yql_query}) + \
                  "&format=json&diagnostics=true&env=store://datatables.org/alltableswithkeys&callback="
        result = urllib.request.urlopen(yql_url).read()
        with open('../../log/test.json','w') as f:
            f.write(json.dumps(json.loads(result)))
        return json.loads(result)
    except Exception as e:
        raise e.with_traceback(e.__traceback__)


if __name__ == '__main__':
    print(EQUITY(['AAPL', 'MSFT']))