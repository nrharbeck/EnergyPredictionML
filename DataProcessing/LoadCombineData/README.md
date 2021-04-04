These files are used to format the raw DSIRE and EIA data and combine the two sets for modeling.

DSIRE data was downloaded directly from the February 2021 Database Archives (http://www.dsireusa.org/resources/database-archives/). The raw files are all saved within the DataProcessing folder

Start by obtaining a key from the EIA API (https://www.eia.gov/opendata/) and running the "EIA_Annual_Loading.py" file (or "EIA_Monthly_Loading.py" if you wish to pull in monthly data).

Then, the EIA and DSIRE preprocessing python files can be used to format the raw data into something useful. 

Finally, the "Combine_EIA_DSIRE.py" file merges the two datasets into one table for analysis. This table has already been saved as "EIA_DSIRE_Data_Tech.csv" in the DataProcessing folder for easy access.

