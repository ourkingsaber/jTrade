CREATE TABLE `jTrade_dev`.`EquityQuote` (
  `symbol` VARCHAR(45) NOT NULL,
  `time` DATETIME NOT NULL,
  `price` FLOAT NULL,
  `change` FLOAT NULL,
  `pct_change` FLOAT NULL,
  `volume` FLOAT NULL,
  `avg_volume` FLOAT NULL,
  `name` VARCHAR(45) NULL,
  `exchange` VARCHAR(45) NULL,
  `market_cap` FLOAT NULL,
  `day_high` FLOAT NULL,
  `day_low` FLOAT NULL,
  `year_high` FLOAT NULL,
  `year_low` FLOAT NULL,
  PRIMARY KEY (`symbol`, `time`));

CREATE TABLE `jTrade_dev`.`Position` (
  `symbol` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `share` FLOAT NOT NULL,
  `price` FLOAT NOT NULL,
  `value` FLOAT NULL,
  `cost` FLOAT NULL,
  `pct_ret` FLOAT NULL,
  `abs_ret` FLOAT NULL,
  PRIMARY KEY (`symbol`, `date`));

CREATE TABLE `jTrade_dev`.`Order` (
  `symbol` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `share` FLOAT NULL,
  `price` FLOAT NULL,
  `fee` FLOAT NULL,
  `total` FLOAT NULL,
  PRIMARY KEY (`symbol`, `date`));

CREATE TABLE `jTrade_dev`.`EquityHP` (
  `symbol` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `open` FLOAT NULL,
  `high` FLOAT NULL,
  `low` FLOAT NULL,
  `close` FLOAT NULL,
  `volume` FLOAT NULL,
  `adjusted` FLOAT NULL,
  PRIMARY KEY (`symbol`, `date`));

CREATE TABLE `jTrade_dev`.`EquityInd` (
  `symbol` VARCHAR(45) NOT NULL,
  `date` DATE NOT NULL,
  `indicator` VARCHAR(45) NOT NULL,
  `val` FLOAT NULL,
  PRIMARY KEY (`symbol`, `date`, `indicator`));
