import datetime
import numpy as np
import pandas as pd
from collections import OrderedDict


def isotodate(isostr):
    return datetime.datetime.strptime(isostr, '%Y-%m-%d').date()

def date_to_np(dt_date : datetime.date):
    return np.datetime64(dt_date)


def np_to_date(np_date : np.datetime64):
    iso = np.datetime_as_string(np_date)
    return datetime.datetime.strptime(iso, '%Y-%m-%d').date()


def time_to_np(dt_datetime : datetime.datetime):
    return np.datetime64(dt_datetime)


def np_to_time(np_datetime : np.datetime64):
    iso = np.datetime_as_string(np_datetime)
    return datetime.datetime.strptime(iso, '%Y-%m-%dT%H:%M:%S')

def ordereddict_to_dataframe(od : OrderedDict, idx_col='date'):
    df = pd.DataFrame.from_dict(od, orient='index')
    return df

def dataframe_to_ordereddict(df : pd.DataFrame):
    return df.to_dict('index')

if __name__ == '__main__':
    # print(date_to_np(datetime.date.today()))
    # print(np_to_date(np.datetime64('2017-01-01')))
    # print(time_to_np(datetime.datetime.now()))
    # print(np.datetime64(datetime.date.today()))
    # print(np_to_time(np.datetime64('2005-02-25T03:30:01')))
    od = OrderedDict()
    od[datetime.date(2017,1,1)] = {'symbol': 'AAPL', 'date': datetime.date(2017, 1, 1), 'share': 100, 'price': 100, 'fee': 10, 'total': 10010}
    od[datetime.date(2017,1,2)] =  {'symbol': 'AAPL', 'date': datetime.date(2017, 1, 2), 'share': -50, 'price': 100, 'fee': 10, 'total': -4990}
    print(ordereddict_to_dataframe(od))
    print(dict(od))