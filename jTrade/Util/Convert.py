import datetime
import numpy as np

def date_to_np(dt_date : datetime.date):
    try:
        return np.datetime64(dt_date)
    except Exception as e:
        raise e.with_traceback(e.__traceback__)

def np_to_date(np_date : np.datetime64):
    try:
        iso = np.datetime_as_string(np_date)
        return datetime.datetime.strptime(iso, '%Y-%m-%d').date()
    except Exception as e:
        raise e.with_traceback(e.__traceback__)

def time_to_np(dt_datetime : datetime.datetime):
    try:
        return np.datetime64(dt_datetime)
    except Exception as e:
        raise e.with_traceback(e.__traceback__)

def np_to_time(np_datetime : np.datetime64):
    try:
        iso = np.datetime_as_string(np_datetime)
        return datetime.datetime.strptime(iso, '%Y-%m-%dT%H:%M:%S')
    except Exception as e:
        raise e.with_traceback(e.__traceback__)

if __name__ == '__main__':
    print(date_to_np(datetime.date.today()))
    print(np_to_date(np.datetime64('2017-01-01')))
    print(time_to_np(datetime.datetime.now()))
    print(np.datetime64(datetime.date.today()))
    print(np_to_time(np.datetime64('2005-02-25T03:30:01')))