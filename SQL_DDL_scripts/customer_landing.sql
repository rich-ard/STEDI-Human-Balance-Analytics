CREATE EXTERNAL TABLE IF NOLT EXISTS `stedi`.`customer_landing` (
  `serialnumber` string,
  `sharewithpublicasofdate` bigint,
  `birthday` string,
  `registrationdate` bigint,
  `sharewithresearchasofdate` bigint,
  `customername` string,
  `email` string,
  `lastupdatedate` bigint,
  `phone` string,
  `sharewithfriendsasofdate` bigint
  )
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = `
) LOCATION 's3://frequently-modulated-lakehouse/customer/landing'
TBLPROPERTIES ('has_encrypted_data'='false');
