# STEDI-Human-Balance-Analytics
Public repo for WGU/Udacity D609 "Data Analytics at Scale" AWS/Spark/Glue assignment. Project rubric addressed as follows:

## Required files

Required python files at top level of repository:
- customer_landing_to_trusted.py
- accelerometer_landing_to_trusted.py
- step_trainer_trusted.py
- customer_trusted_to_curated.py
- machine_learning_curated.py

SQL queries in SQL_DDL_scripts directory:
-  customer_landing.sql
-  accelerometer_landing.sql
-  step_trainer_landing.sql

## Screenshots
### Landing Zone

![Count of customer_landing: 956 rows](./screenshot_png_files/count_of_customer_landing.png)
![The customer_landing data contains multiple rows with a blank shareWithResearchAsOfDate.](./screenshot_png_files/null_results_for_shareWithResearchAsOfDate.png)
![Count of accelerometer_landing: 81273 rows](./screenshot_png_files/count_of_accelerometer_landing.png)
![Count of step_trainer_landing: 28680 rows](./screenshot_png_files/count_of_step_trainer_landing.png)

### Trusted Zone

![Count of customer_trusted: 482 rows where shareWithResearchAsOfDate is not blank](./screenshot_png_files/count_of_customer_trusted.png)
![Count of accelerometer_trusted: 40981 rows](./screenshot_png_files/count_of_accelerometer_trusted.png)
![Count of step_trainer_trusted: 14460 rows](./screenshot_png_files/count_of_step_trainer_trusted.png)

### Curated Zone

Screenshots:
![Count of customer_curated: 482 rows](./screenshot_png_files/count_of_customer_curated.png)
![Count of machine_learning_curated: 43681 rows](./screenshot_png_files/count_of_machine_learning_curated.png)
