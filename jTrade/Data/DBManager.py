import datetime

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import and_, or_, select

import Data.Table
import Util.Const
import Util.Convert
import Util.Credential


class DBManager(object):
    """
    Database manager responsible for interaction with sql db.
    """

    _logic_op = {'&', '|'}
    _filter_op = {'=', '!=', '>', '<', '>=', '<='}

    def __init__(self, info : dict= Util.Credential.local_dev_db):
        self._engine = create_engine('{}://{}:{}@{}:{}/{}'.format(info['type'], info['user'], info['pw'],
                                                                  info['host'], info['port'], info['db']))
        self._DBSession = sessionmaker(bind=self._engine)

    def select(self, table : Data.Table.Table, filter_dict, index_col='date', parse_dates=['date']):
        sql_filter = DBManager.dict_to_sql_filter(table, filter_dict)
        s = select([table]).where(sql_filter)
        if parse_dates:
            df = pd.read_sql(s, self._engine, index_col=index_col, parse_dates=parse_dates)
        else:
            df = pd.read_sql(s, self._engine)
        return df

    def insert(self, table : Data.Table.Table, values_list):
        conn = self._engine.connect()
        if not isinstance(values_list, list):
            values_list = [values_list]
        for values in values_list:
            ins = table.insert().values(**values)
            conn.execute(ins)
        conn.close()

    def insert_df(self, table : Data.Table.Table, dataframe : pd.DataFrame, if_exists='append', index=False):
        """Inserts a dataframe into database.

        :param table:
        :param dataframe:
        :param if_exists: fail, replace, append
        :param index: if True, insert index as a column
        :return:
        """
        dtype = {str(col.description): col.type for col in table.columns}
        dataframe.to_sql(str(table.name), self._engine, schema=self._engine.url.database,
                         if_exists=if_exists, index=index, dtype=dtype)

    @staticmethod
    def dict_to_sql_filter(table : Data.Table.Table, filter_dict : dict):
        """
        :param table: python class.
        :param filter_dict: {'&': {('symbol','='): 'AAPL', ('date', '>'): datetime.date(2017,1,1)}}
        :return: sqlalchemy expression
        """
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

# common DBManager for application
# todo: check if this is the general approach
dbmanager = DBManager(Util.Credential.local_dev_db)


if __name__ == '__main__':
    filtr = {'&': {('symbol', '='): 'AAPL',
                   ('date', '='): datetime.date(2017,8,21)}}
    test = dbmanager.select(Data.Table.EquityHP, filtr)
    print(test)
    #
    filtr = {('date', '='): datetime.date(2017, 8, 21)}
    tests = dbmanager.select(Data.Table.EquityHP, filtr)
    print(tests)

    # res = dbmanager.select(Data.DB.Table.EquityHP, {('symbol','='):'AAPL'})
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
    dbmanager.insert_df(Data.Table.Position, df, 'append', False)