import datetime
import numpy as np
import pandas as pd
from collections import OrderedDict


# def date_to_np(dt_date : datetime.date):
#     try:
#         return np.datetime64(dt_date)
#     except Exception as e:
#         raise e.with_traceback(e.__traceback__)
#
#
# def np_to_date(np_date : np.datetime64):
#     try:
#         iso = np.datetime_as_string(np_date)
#         return datetime.datetime.strptime(iso, '%Y-%m-%d').date()
#     except Exception as e:
#         raise e.with_traceback(e.__traceback__)
#
#
# def time_to_np(dt_datetime : datetime.datetime):
#     try:
#         return np.datetime64(dt_datetime)
#     except Exception as e:
#         raise e.with_traceback(e.__traceback__)
#
#
# def np_to_time(np_datetime : np.datetime64):
#     try:
#         iso = np.datetime_as_string(np_datetime)
#         return datetime.datetime.strptime(iso, '%Y-%m-%dT%H:%M:%S')
#     except Exception as e:
#         raise e.with_traceback(e.__traceback__)

def ordereddict_to_dataframe(od : OrderedDict, idx_col='date'):
    try:

        df = pd.DataFrame.from_dict(od, orient='index')
        return df
    except Exception as e:
        raise e.with_traceback(e.__traceback__)

def dataframe_to_ordereddict(df : pd.DataFrame):
    try:
        return df.to_dict('index')
    except Exception as e:
        raise e.with_traceback(e.__traceback__)

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