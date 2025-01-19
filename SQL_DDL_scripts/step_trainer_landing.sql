CREATE EXTERNAL TABLE IF NOT EXISTS `stedi`.`step_trainer_landing` (
`sensorreadingtime` bigint
, `serialnumber` string
, `distancefromobject` int
  )
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = `
) LOCATION 's3://frequently-modulated-lakehouse/step_trainer/landing'
TBLPROPERTIES ('has_encrypted_data'='false');
