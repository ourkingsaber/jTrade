from sqlalchemy import Table, Column, MetaData, Float, String, Date, DateTime, Integer

_metadata = MetaData()


# Daily equity historical price
EquityHP = Table(
    'EquityHP', _metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('date', Date(), primary_key=True),
    Column('open', Float()),
    Column('high', Float()),
    Column('low', Float()),
    Column('close', Float()),
    Column('volume', Float()),
    Column('ex_dividend', Float()),
    Column('split_ratio', Float()),
    Column('adj_open', Float()),
    Column('adj_high', Float()),
    Column('adj_low', Float()),
    Column('adj_close', Float()),
    Column('adj_volume', Float())
)
EquityHP_flds = list(EquityHP.columns.keys())
EquityHP_idxs = {name: idx for idx, name in enumerate(EquityHP.columns.keys())}


# Equity real time quote
EquityQuote = Table(
    'EquityQuote', _metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('time', DateTime(), primary_key=True),
    Column('price', Float()),
    Column('change', Float()),
    Column('pct_change', Float()),
    Column('volume', Float()),
    Column('avg_volume', Float()),
    Column('name', String(collation='utf8')),
    Column('exchange', String(collation='utf8')),
    Column('market_cap', Float()),
    Column('day_high', Float()),
    Column('day_low', Float()),
    Column('year_high', Float()),
    Column('year_low', Float())
)
EquityQuote_flds = list(EquityQuote.columns.keys())


# Position historical record
Position = Table(
    'Position', _metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('date', Date(), primary_key=True),
    Column('share', Float()),
    Column('price', Float()),
    Column('value', Float()),
    Column('cost', Float()),
    Column('pct_ret', Float()),
    Column('abs_ret', Float())
)
Position_flds = list(Position.columns.keys())


# Order record
Order = Table(
    'Order', _metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('date', Date(), primary_key=True),
    Column('share', Float()),
    Column('price', Float()),
    Column('fee', Float()),
    Column('total', Float())
)
Order_flds = list(Order.columns.keys())


# Equity daily technical indicator
EquityInd = Table(
    'EquityInd1d', _metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('date', Date(), primary_key=True),
    Column('indicator', String(collation='utf8'), primary_key=True),
    Column('val', Float())
)
EquityInd_flds = list(EquityInd.columns.keys())


EquityFinIS = Table(
    'EquityFinIS', _metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('year', Integer(), primary_key=True),
    Column('period', String(collation='utf8'), primary_key=True),
    Column('operatingrevenue', Float()),
    Column('totalrevenue', Float()),
    Column('operatingcostofrevenue', Float()),
    Column('totalcostofrevenue', Float()),
    Column('totalgrossprofit', Float()),
    Column('sgaexpense', Float()),
    Column('rdexpense', Float()),
    Column('totaloperatingexpenses', Float()),
    Column('totaloperatingincome', Float()),
    Column('otherincome', Float()),
    Column('totalotherincome', Float()),
    Column('totalpretaxincome', Float()),
    Column('incometaxexpense', Float()),
    Column('netincomecontinuing', Float()),
    Column('netincome', Float()),
    Column('netincometocommon', Float()),
    Column('weightedavebasicsharesos', Float()),
    Column('basiceps', Float()),
    Column('weightedavedilutedsharesos', Float()),
    Column('dilutedeps', Float()),
    Column('weightedavebasicdilutedsharesos', Float()),
    Column('basicdilutedeps', Float()),
    Column('cashdividendspershare', Float())
)


EquityFinBS = Table(
    'EquityFinBS', _metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('year', Integer(), primary_key=True),
    Column('period', String(collation='utf8'), primary_key=True),
    Column('cashandequivalents', Float()),
    Column('shortterminvestments', Float()),
    Column('notereceivable', Float()),
    Column('accountsreceivable', Float()),
    Column('netinventory', Float()),
    Column('othercurrentassets', Float()),
    Column('totalcurrentassets', Float()),
    Column('netppe', Float()),
    Column('longterminvestments', Float()),
    Column('goodwill', Float()),
    Column('intangibleassets', Float()),
    Column('othernoncurrentassets', Float()),
    Column('totalnoncurrentassets', Float()),
    Column('totalassets', Float()),
    Column('shorttermdebt', Float()),
    Column('accountspayable', Float()),
    Column('accruedexpenses', Float()),
    Column('totalcurrentliabilities', Float()),
    Column('longtermdebt', Float()),
    Column('othernoncurrentliabilities', Float()),
    Column('totalnoncurrentliabilities', Float()),
    Column('totalliabilities', Float()),
    Column('commitmentsandcontingencies', Float()),
    Column('commonequity', Float()),
    Column('retainedearnings', Float()),
    Column('aoci', Float()),
    Column('totalcommonequity', Float()),
    Column('totalequity', Float()),
    Column('totalequityandnoncontrollinginterests', Float()),
    Column('totalliabilitiesandequity', Float()),
    Column('currentdeferredrevenue', Float()),
    Column('noncurrentdeferredrevenue', Float()),
    Column('currentdeferredtaxassets', Float())
)


EquityFinCF = Table(
    'EquityFinCF', _metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('year', Integer(), primary_key=True),
    Column('period', String(collation='utf8'), primary_key=True),
    Column('netincome', Float()),
    Column('netincomecontinuing', Float()),
    Column('depreciationexpense', Float()),
    Column('noncashadjustmentstonetincome', Float()),
    Column('increasedecreaseinoperatingcapital', Float()),
    Column('netcashfromcontinuingoperatingactivities', Float()),
    Column('netcashfromoperatingactivities', Float()),
    Column('purchaseofplantpropertyandequipment', Float()),
    Column('acquisitions', Float()),
    Column('purchaseofinvestments', Float()),
    Column('saleofinvestments', Float()),
    Column('otherinvestingactivitiesnet', Float()),
    Column('netcashfromcontinuinginvestingactivities', Float()),
    Column('netcashfrominvestingactivities', Float()),
    Column('repurchaseofcommonequity', Float()),
    Column('paymentofdividends', Float()),
    Column('issuanceofdebt', Float()),
    Column('repaymentofdebt', Float()),
    Column('issuanceofcommonequity', Float()),
    Column('otherfinancingactivitiesnet', Float()),
    Column('netcashfromcontinuingfinancingactivities', Float()),
    Column('netcashfromfinancingactivities', Float()),
    Column('netchangeincash', Float()),
    Column('cashinterestpaid', Float()),
    Column('cashincometaxespaid', Float())
)


EquityFinFund = Table(
    'EquityFinFund', _metadata,
    Column('symbol', String(collation='utf8'), primary_key=True),
    Column('year', Integer(), primary_key=True),
    Column('period', String(collation='utf8'), primary_key=True),
    Column('revenuegrowth', Float()),
    Column('nopat', Float()),
    Column('nopatmargin', Float()),
    Column('investedcapital', Float()),
    Column('investedcapitalturnover', Float()),
    Column('investedcapitalincreasedecrease', Float()),
    Column('freecashflow', Float()),
    Column('netnonopex', Float()),
    Column('netnonopobligations', Float()),
    Column('ebit', Float()),
    Column('depreciationandamortization', Float()),
    Column('ebitda', Float()),
    Column('capex', Float()),
    Column('dfcfnwc', Float()),
    Column('dfnwc', Float()),
    Column('nwc', Float()),
    Column('debt', Float()),
    Column('ltdebtandcapleases', Float()),
    Column('netdebt', Float()),
    Column('totalcapital', Float()),
    Column('bookvaluepershare', Float()),
    Column('tangbookvaluepershare', Float()),
    Column('marketcap', Float()),
    Column('enterprisevalue', Float()),
    Column('pricetobook', Float()),
    Column('pricetotangiblebook', Float()),
    Column('pricetorevenue', Float()),
    Column('pricetoearnings', Float()),
    Column('dividendyield', Float()),
    Column('earningsyield', Float()),
    Column('evtoinvestedcapital', Float()),
    Column('evtorevenue', Float()),
    Column('evtoebitda', Float()),
    Column('evtoebit', Float()),
    Column('evtonopat', Float()),
    Column('evtoocf', Float()),
    Column('evtofcff', Float()),
    Column('ebitdagrowth', Float()),
    Column('ebitgrowth', Float()),
    Column('nopatgrowth', Float()),
    Column('netincomegrowth', Float()),
    Column('epsgrowth', Float()),
    Column('ocfgrowth', Float()),
    Column('fcffgrowth', Float()),
    Column('investedcapitalgrowth', Float()),
    Column('revenueqoqgrowth', Float()),
    Column('ebitdaqoqgrowth', Float()),
    Column('ebitqoqgrowth', Float()),
    Column('nopatqoqgrowth', Float()),
    Column('netincomeqoqgrowth', Float()),
    Column('epsqoqgrowth', Float()),
    Column('ocfqoqgrowth', Float()),
    Column('fcffqoqgrowth', Float()),
    Column('investedcapitalqoqgrowth', Float()),
    Column('grossmargin', Float()),
    Column('ebitdamargin', Float()),
    Column('operatingmargin', Float()),
    Column('ebitmargin', Float()),
    Column('profitmargin', Float()),
    Column('costofrevtorevenue', Float()),
    Column('sgaextorevenue', Float()),
    Column('rdextorevenue', Float()),
    Column('opextorevenue', Float()),
    Column('taxburdenpct', Float()),
    Column('interestburdenpct', Float()),
    Column('efftaxrate', Float()),
    Column('assetturnover', Float()),
    Column('arturnover', Float()),
    Column('invturnover', Float()),
    Column('faturnover', Float()),
    Column('apturnover', Float()),
    Column('dso', Float()),
    Column('dio', Float()),
    Column('dpo', Float()),
    Column('ccc', Float()),
    Column('finleverage', Float()),
    Column('leverageratio', Float()),
    Column('compoundleveragefactor', Float()),
    Column('ltdebttoequity', Float()),
    Column('debttoequity', Float()),
    Column('roic', Float()),
    Column('nnep', Float()),
    Column('roicnnepspread', Float()),
    Column('rnnoa', Float()),
    Column('roe', Float()),
    Column('croic', Float()),
    Column('oroa', Float()),
    Column('roa', Float()),
    Column('noncontrollinginterestsharingratio', Float()),
    Column('roce', Float()),
    Column('divpayoutratio', Float()),
    Column('augmentedpayoutratio', Float()),
    Column('ocftocapex', Float()),
    Column('stdebttocap', Float()),
    Column('ltdebttocap', Float()),
    Column('debttototalcapital', Float()),
    Column('preferredtocap', Float()),
    Column('noncontrolinttocap', Float()),
    Column('commontocap', Float()),
    Column('debttoebitda', Float())
)