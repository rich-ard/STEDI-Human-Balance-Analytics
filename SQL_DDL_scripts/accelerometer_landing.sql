CREATE EXTERNAL TABLE IF NOLT EXISTS `stedi`.`accelerometer_landing` (
  `user` string
  , `timeStamp` bigint
  , `x` float
  , `y` float
  , `z` float
  )
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = `
) LOCATION 's3://frequently-modulated-lakehouse/accelerometer/landing'
TBLPROPERTIES ('has_encrypted_data'='false');
