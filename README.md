# Data Analytics Migration Tableau

## Data Wrangling and Cleaning
- Created 9 Pandas dataframes from 9 csv files of flight information for the years 1987-1996
- Cleared any columns that contained all NaN values, then replaced any remaining NaN values with 0
- Concatenated the dataframes to produce a master dataframe. The 1995 and 1996 had 4 columns of extra data so these were discarded. If kept, 75% of the entries in these columns would have been NaN
- Exported the dataframe to a csv and uploaded it to an S3 bucket

## PostgreSQL RDS data import and reporting
- Connected an RDS database to pgadmin4 and established a server with a 'flights' table
- Imported the combined_data.csv into the flights table and used SQL statements to calculate the following statistics:
    - How many total records does the table contain? 
        **42722968**
    - Does it have the same number of records as those in the combined_data.csv file?
        **Yes**
    - Which year had the most number of total inbound and outbound flights? 
        **1996 with 5351983 flights**
    -  Which country is the most popular destination for flights?
        **ORD with 2326296 flights**

## Integrate Tableau Desktop with Amazon RDS and produce reports
- Entered admin details for the Amazon RDS and updated to have the current form of the data in Tableau
- Created a chart that displays the historical data for the highest flight destinations, searchable by year with a filter
- Created a bar chart that shows the average distance that airplanes travel for all flights for each carrier, searchable by year with a filter
- Created a line chart that shows the top most used flight numbers and found the most popular origins and destinations for each:
    1. **505** ORIGIN: *ORD* DESTINATION: *MCI*
    2. **409** ORIGIN: *LGA* DESTINATION: *DFW*
    3. **440** ORIGIN: *PHX* DESTINATION: *PHX*
    4. **456** ORIGIN: *PHX* DESTINATION: *PHX*
    5. **711** ORIGIN: *JFK* DESTINATION: *LAS*
- Created a dashboard with graphs showing total arrival delay, average departure delay and total cancellations for all airports
