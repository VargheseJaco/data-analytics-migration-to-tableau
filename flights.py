#%%
import boto3
import glob
import numpy as np
import os
import pandas as pd
#%%
#Change path to relevant path on your machine
path = '/Users/varghesejacob/Desktop/AiCore/Migration_Project/data-analytics-files' 
all_csv_files_sorted = sorted(glob.glob(os.path.join(path, "*.csv")))

#original copy retained for testing purposes
dataframes_original = [pd.read_csv(i) for i in all_csv_files_sorted]

dataframes = dataframes_original

#drops columns that are completely NaN and replaced remaining NaNs with 0
dataframes = [i.dropna(axis=1, how='all') for i in dataframes]
dataframes = [i.fillna(0) for i in dataframes]

#concatenates all the dataframes into one then exports it to a csv
master_dataframe = pd.concat(dataframes, axis=0)
master_dataframe_cleaned = master_dataframe.dropna(axis=1, how='any')

master_dataframe_cleaned.to_csv('combined_data.csv', index=False )

# %%
#uploads to s3 bucket
s3 = boto3.client('s3')
s3.upload_file('/Users/varghesejacob/Desktop/AiCore/Migration_Project/combined_data.csv', 'my-boto3-bucket-varghese', 'combined_data.csv')
#%%