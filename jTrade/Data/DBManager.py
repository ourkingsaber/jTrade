
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import Util.Const

class DBManager(object):
    """
    Data base manager responsible for interaction with sql db.
    """

    def __init__(self, info : dict):
        try:
            self._engine = create_engine('{}://{}:{}@{}:{}/{}'.format(info['type'], info['user'], info['pw'],
                                                                      info['host'], info['port'], info['db']))
            self._DBSession = sessionmaker(bind=self._engine)
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def add(self, object):
        try:
            session = self._DBSession()
            if isinstance(object, list):
                for obj in object:
                    session.add(obj)
            else:
                session.add(object)
            session.commit()
            session.close()
        except Exception as e:
            raise e.with_traceback(e.__traceback__)

    def query(self, cls, id):
        try:
            session = self._DBSession()
            obj = session.query(cls).filter(cls.id==id).one()
            session.close()
            return obj
        except Exception as e:
            raise e.with_traceback(e.__traceback__)


if __name__ == '__main__':
    from sqlalchemy.ext.declarative import declarative_base
    dbm = DBManager(Util.Const.LOCAL_TEST_INFO)

    # 创建对象的基类:
    Base = declarative_base()


    # 定义User对象:
    class User(Base):
        # 表的名字:
        __tablename__ = 'user'

        # 表的结构:
        id = Column(Integer, primary_key=True)
        name = Column(String(45))


    # new_user = User(id='5', name='Bob')
    # dbm.add(new_user)
    user = dbm.query(User, 'Joker')
    print(user.id)