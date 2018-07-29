import json
import datetime
from jTrade.data.db_manager import DBManager
from jTrade.data.fetch import Quandl
from jTrade.data.table import EquityHP
import jTrade.Util.Credential as Credential
from jTrade.Util.log import get_logger
from jTrade.Util.exception import *

logfile = '../Log/GetHP-{}.log'.format(datetime.date.today().isoformat())
open(logfile, 'a+').close()
logger = get_logger('getfin', logfile)


dbmanager = DBManager(Credential.default_db)
firstdate = dbmanager.execute('SELECT distinct date FROM jTrade.EquityHP a order by date desc limit 1')[0][0] + datetime.timedelta(1)

all_syms = dbmanager.execute('select distinct symbol from EquityHP')
all_syms = [x[0] for x in all_syms]

lastdate = datetime.date.today()
batchsize = 5
for i in range(len(all_syms) // batchsize + 1):
    batch = all_syms[i*batchsize: (i+1)*batchsize]
    try:
        newhpdf = Quandl.EquityHP(batch, firstdate, lastdate)
        dbmanager.insert_df(EquityHP, newhpdf)
        logger.info('Inserted HP from {} to {} for {}'.format(firstdate, lastdate, ', '.join(batch)))
    except Exception as e:
        logger.error('{}: {}'.format(type(e).__name__, e))

