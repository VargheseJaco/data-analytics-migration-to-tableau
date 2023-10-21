# Data Analytics Migration Tableau

## Data Wrangling and Cleaning
- Created 9 Pandas dataframes from 9 csv files of flight information for the years 1987-1996
- Cleared any columns that contained all NaN values, then replaced any remaining NaN values with 0
- Concatenated the dataframes to produce a master dataframe. The 1995 and 1996 had 4 columns of extra data so these were discarded. If kept, 75% of the entries in these columns would have been NaN
- Exported the dataframe to a csv and uploaded it to an S3 bucket

