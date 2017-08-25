import datetime
import numpy as np
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import and_, or_, not_, select
import Util.Const
import Util.Convert
import Data.DB.Table


class DBManager(object):
    """
    Data base manager responsible for interaction with sql db.
    """

    _logic_op = {'&', '|'}
    _filter_op = {'=', '!=', '>', '<', '>=', '<='}

    def __init__(self, info : dict=Util.Const.LOCAL_DEV_INFO):
        try:
            self._engine = create_engine('{}://{}:{}@{}:{}/{}'.format(info['type'], info['user'], info['pw'],
                                                                      info['host'], info['port'], info['db']))
            self._DBSession = sessionmaker(bind=self._engine)
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def select(self, table : Data.DB.Table.Table, filter_dict, index_col='date', parse_dates=['date']):
        try:
            sql_filter = DBManager.dict_to_sql_filter(table, filter_dict)
            s = select([table]).where(sql_filter)
            df = pd.read_sql(s, self._engine, index_col=index_col, parse_dates=parse_dates)
            return df
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def insert(self, table : Data.DB.Table.Table, values_list):
        try:
            conn = self._engine.connect()
            if not isinstance(values_list, list):
                values_list = [values_list]
            for values in values_list:
                ins = table.insert().values(**values)
                conn.execute(ins)
            conn.close()
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def insert_df(self, table : Data.DB.Table.Table, dataframe : pd.DataFrame, if_exists='append', index=False):
        """Inserts a dataframe into database.

        :param table:
        :param dataframe:
        :param if_exists: fail, replace, append
        :param index: if True, insert index as a column
        :return:
        """
        try:
            dtype = {str(col.description): col.type for col in table.columns}
            dataframe.to_sql(str(table.name), self._engine, schema=self._engine.url.database,
                             if_exists=if_exists, index=index, dtype=dtype)
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    @staticmethod
    def dict_to_sql_filter(table : Data.DB.Table.Table, filter_dict : dict):
        """
        :param table: python class.
        :param filter_dict: {'&': {('symbol','='): 'AAPL', ('date', '>'): datetime.date(2017,1,1)}}
        :return: sqlalchemy expression
        """
        try:
            if len(list(filter_dict.keys())) != 1:
                raise ValueError('filter dict not valid. Number of items should be 1')
            k, v = next(iter(filter_dict.items()))
            if k in DBManager._logic_op:
                child_filters = (DBManager.dict_to_sql_filter(table, {k: v}) for k, v in v.items())
                if k == '&':
                    sql_filter = and_(*child_filters)
                elif k == '|':
                    sql_filter = or_(*child_filters)
                else:
                    raise ValueError('{} is not a valid operator'.format(k))
            else:
                if k[1] == '=':
                    sql_filter = table.columns[k[0]] == v
                elif k[1] == '!=':
                    sql_filter = table.columns[k[0]] != v
                elif k[1] == '>':
                    sql_filter = table.columns[k[0]] > v
                elif k[1] == '<':
                    sql_filter = table.columns[k[0]] < v
                elif k[1] == '>=':
                    sql_filter = table.columns[k[0]] >= v
                elif k[1] == '<=':
                    sql_filter = table.columns[k[0]] <= v
                else:
                    raise ValueError('{} is not a valid operator'.format(k))
            return sql_filter
        except Exception as e:
            raise e.with_traceback(e.__traceback__)


if __name__ == '__main__':
    dm = DBManager()
    filtr = {'&': {('symbol', '='): 'AAPL',
                   ('date', '='): datetime.date(2017,8,21)}}
    test = dm.select(Data.DB.Table.EquityHP1d, filtr)
    print(test)
    #
    filtr = {('date', '='): datetime.date(2017, 8, 21)}
    tests = dm.select(Data.DB.Table.EquityHP1d, filtr)
    print(tests)

    # res = dm.select(Data.DB.Table.EquityHP1d, {('symbol','='):'AAPL'})
    # for row in res:
    #     print(row)

    df = pd.DataFrame({
        'symbol': ['CASH1', 'CASH2'],
        'date': [datetime.date.today(), datetime.date.today()],
        'share': [123,345],
        'price': [100, 200],
        'value': [12300,69000],
        'cost': [100,200],
        'pct_ret': [0,0],
        'abs_ret': [0,0]
    })
    dm.insert_df(Data.DB.Table.Position, df, 'append', False)