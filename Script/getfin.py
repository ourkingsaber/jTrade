import json
import logging
from Data.DBManager import DBManager
from Data.Fetch import Intrinio, Quandl
from Data.Table import EquityFinIS, EquityFinBS, EquityFinCF, EquityFinFund
import Util.Credential
from Util.Logging import logger
from Util.ErrorHandling import *

logging.basicConfig(filename='../Log/GetFin.log')

with open('../Log/EquityFinFinishedSymbols.json', 'r') as f:
    finished_symbols = set(json.load(f))
with open('../Log/EquityFinNoData.json', 'r') as f:
    nodata = set(json.load(f))

dbmanager = DBManager(Util.Credential.aws_db)
all_syms = dbmanager.execute('select distinct symbol from EquityHP')
all_syms = [x[0] for x in all_syms]

existing_bs = set(map(tuple,dbmanager.execute('select symbol, year, period from EquityFinBS')))
existing_is = set(map(tuple,dbmanager.execute('select symbol, year, period from EquityFinIS')))
existing_cf = set(map(tuple,dbmanager.execute('select symbol, year, period from EquityFinCF')))
existing_fund = set(map(tuple,dbmanager.execute('select symbol, year, period from EquityFinFund')))

periods = ('FY', 'Q1', 'Q2', 'Q3', 'Q4', 'Q1TTM', 'Q2TTM', 'Q3TTM', 'Q2YTD', 'Q3YTD')
bsperiods = ('FY', 'Q1', 'Q2', 'Q3', 'Q4')
count = 0
for symbol in all_syms:
    if symbol in finished_symbols:
        continue
    err = False
    for year in range(2009, 2018):
        for period in periods:
            if (symbol, year, period) not in existing_is and (symbol, year, period, 'income_statement') not in nodata:
                try:
                    resdf = Intrinio.EquityFin(symbol, year, period, 'income_statement')
                    count += 1
                    dbmanager.insert_df(EquityFinIS, resdf)
                    print('Inserted {}'.format((symbol, year, period, 'income_statement')))
                except NoDataError as e:
                    nodata.add((symbol, year, period, 'income_statement'))
                except Exception as e:
                    err = True
                    logger.error(e.with_traceback(e.__traceback__))
            if (symbol, year, period) not in existing_cf and (symbol, year, period, 'cash_flow_statement') not in nodata:
                try:
                    resdf = Intrinio.EquityFin(symbol, year, period, 'cash_flow_statement')
                    count += 1
                    dbmanager.insert_df(EquityFinCF, resdf)
                    print('Inserted {}'.format((symbol, year, period, 'cash_flow_statement')))
                except NoDataError as e:
                    nodata.add((symbol, year, period, 'cash_flow_statement'))
                except Exception as e:
                    err = True
                    logger.error(e.with_traceback(e.__traceback__))
            if (symbol, year, period) not in existing_fund and (symbol, year, period, 'calculations') not in nodata:
                try:
                    resdf = Intrinio.EquityFin(symbol, year, period, 'calculations')
                    count += 1
                    dbmanager.insert_df(EquityFinFund, resdf)
                    print('Inserted {}'.format((symbol, year, period, 'calculations')))
                except NoDataError as e:
                    nodata.add((symbol, year, period, 'calculations'))
                except Exception as e:
                    err = True
                    logger.error(e.with_traceback(e.__traceback__))
        for period in bsperiods:
            if (symbol, year, period) not in existing_bs and (symbol, year, period, 'balance_sheet') not in nodata:
                try:
                    resdf = Intrinio.EquityFin(symbol, year, period, 'balance_sheet')
                    count += 1
                    dbmanager.insert_df(EquityFinBS, resdf)
                    print('Inserted {}'.format((symbol, year, period, 'balance_sheet')))
                except NoDataError as e:
                    nodata.add((symbol, year, period, 'balance_sheet'))
                except Exception as e:
                    err = True
                    logger.error(e.with_traceback(e.__traceback__))
        if count > 10:
            break
    if not err:
        finished_symbols.add(symbol)
    if count > 10:
        break

with open('../Log/EquityFinFinishedSymbols.json', 'w') as f:
    json.dump(list(finished_symbols), f)
with open('../Log/EquityFinNoData.json', 'w') as f:
    json.dump(list(nodata), f)