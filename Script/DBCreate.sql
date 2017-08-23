CREATE TABLE `jTrade_dev`.`EquityQuote` (
  `symbol` VARCHAR(10) NOT NULL,
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
  `symbol` VARCHAR(10) NOT NULL,
  `date` DATE NOT NULL,
  `share` FLOAT NOT NULL,
  `price` FLOAT NOT NULL,
  `value` FLOAT NULL,
  `cost` FLOAT NULL,
  `pct_ret` FLOAT NULL,
  `abs_ret` FLOAT NULL,
  PRIMARY KEY (`symbol`, `date`));

CREATE TABLE `jTrade_dev`.`Trade` (
  `symbol` VARCHAR(10) NOT NULL,
  `date` DATE NOT NULL,
  `share` FLOAT NULL,
  `price` FLOAT NULL,
  PRIMARY KEY (`symbol`, `date`));

CREATE TABLE `jTrade_dev`.`EquityHP` (
  `symbol` VARCHAR(10) NOT NULL,
  `date` DATE NOT NULL,
  `opn` FLOAT NULL,
  `high` FLOAT NULL,
  `low` FLOAT NULL,
  `close` FLOAT NULL,
  `volume` FLOAT NULL,
  PRIMARY KEY (`symbol`, `date`));
