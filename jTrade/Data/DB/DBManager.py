import datetime
import numpy as np

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
    _filter_op = {'=', '>', '<', '>=', '<='}

    def __init__(self, info : dict=Util.Const.LOCAL_DEV_INFO):
        try:
            self._engine = create_engine('{}://{}:{}@{}:{}/{}'.format(info['type'], info['user'], info['pw'],
                                                                      info['host'], info['port'], info['db']))
            self._DBSession = sessionmaker(bind=self._engine)
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def select(self, table, dict_filter):
        try:
            conn = self._engine.connect()
            sql_filter = DBManager.dict_to_filter(table, dict_filter)
            s = select([table]).where(sql_filter)
            result = conn.execute(s)
            arr = np.array([row for row in result])
            result.close()
            return arr
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    @staticmethod
    def dict_to_filter(table, dict_filter : dict):
        """
        :param table: python class.
        :param dict_filter: {'&': {('symbol','='): 'AAPL', ('date', '>'): datetime.date(2017,1,1)}}
        :return: sqlalchemy expression
        """
        try:
            if len(list(dict_filter.keys())) != 1:
                raise ValueError('filter dict not valid. Number of items should be 1')
            exp_k, exp_v = next(iter(dict_filter.items()))
            if exp_k in DBManager._logic_op:
                sql_exprs = (DBManager.dict_to_filter(table, {k: v}) for k, v in exp_v.items())
                if exp_k == '&':
                    sql_expr = and_(*sql_exprs)
                elif exp_v == '|':
                    sql_expr = or_(*sql_exprs)
            else:
                if exp_k[1] == '=':
                    sql_expr = table.columns[exp_k[0]] == exp_v
                elif exp_k[1] == '>':
                    sql_expr = table.columns[exp_k[0]] > exp_v
                elif exp_k[1] == '<':
                    sql_expr = table.columns[exp_k[0]] < exp_v
                elif exp_k[1] == '>=':
                    sql_expr = table.columns[exp_k[0]] >= exp_v
                elif exp_k[1] == '<=':
                    sql_expr = table.columns[exp_k[0]] <= exp_v
            return sql_expr
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def add(self, obj):
        try:
            session = self._DBSession()
            if isinstance(obj, list):
                for obj in obj:
                    session.add(obj)
            else:
                session.add(obj)
            session.commit()
            session.close()
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def query(self, cls, dict_filter, one=False):
        """

        :param cls: python class.
        :param dict_filter: {'&': {('symbol','='): 'AAPL', ('date', '>'): datetime.date(2017,1,1)}}
        :param one: if True, returns object, else List[object]
        :return:
        """
        try:
            sql_filter = DBManager.dict_to_filter(cls, dict_filter)
            session = self._DBSession()
            if one:
                objs = session.query(cls).filter(sql_filter).one()
            else:
                objs = session.query(cls).filter(sql_filter).all()
            session.close()
            return objs
        except Exception as e:
            raise e.with_traceback(e.__traceback__)


if __name__ == '__main__':
    dm = DBManager()
    fil = {'&': {('symbol', '='): 'AAPL',
                 ('date', '='): datetime.date(2017,8,21)}}
    test = dm.select(Data.DB.Table.EquityHP1d, fil)
    print(test)
    #
    fil = {('date', '='): datetime.date(2017,8,21)}
    tests = dm.select(Data.DB.Table.EquityHP1d, fil)
    print(tests)

    # res = dm.select(Data.DB.Table.EquityHP1d, {('symbol','='):'AAPL'})
    # for row in res:
    #     print(row)