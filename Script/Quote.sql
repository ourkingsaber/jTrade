CREATE TABLE `jTrade_dev`.`Quote` (
  `symbol` VARCHAR(10) NOT NULL,
  `time` DATETIME NOT NULL,
  `price` DECIMAL(18,5) NULL,
  `change` DECIMAL(18,5) NULL,
  `volume` DECIMAL(18,2) NULL,
  `avg_volume` DECIMAL(18,2) NULL,
  `name` VARCHAR(45) NULL,
  `exchange` VARCHAR(45) NULL,
  `market_cap` DECIMAL(18,10) NULL,
  `day_high` DECIMAL(18,5) NULL,
  `day_low` DECIMAL(18,5) NULL,
  `year_high` DECIMAL(18,5) NULL,
  `year_low` DECIMAL(18,5) NULL,
  PRIMARY KEY (`symbol`, `time`));

ALTER TABLE `jTrade_dev`.`Quote`
CHANGE COLUMN `price` `price` FLOAT NULL DEFAULT NULL ,
CHANGE COLUMN `change` `change` FLOAT NULL DEFAULT NULL ,
CHANGE COLUMN `volume` `volume` FLOAT NULL DEFAULT NULL ,
CHANGE COLUMN `avg_volume` `avg_volume` FLOAT NULL DEFAULT NULL ,
CHANGE COLUMN `market_cap` `market_cap` FLOAT NULL DEFAULT NULL ,
CHANGE COLUMN `day_high` `day_high` FLOAT NULL DEFAULT NULL ,
CHANGE COLUMN `day_low` `day_low` FLOAT NULL DEFAULT NULL ,
CHANGE COLUMN `year_high` `year_high` FLOAT NULL DEFAULT NULL ,
CHANGE COLUMN `year_low` `year_low` FLOAT NULL DEFAULT NULL ;
