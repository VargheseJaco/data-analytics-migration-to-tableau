#%%
import boto3
import glob
import numpy as np
import os
import pandas as pd

path = '/Users/varghesejacob/Desktop/AiCore/Migration_Project/data-analytics-files' 
all_csv_files_sorted = sorted(glob.glob(os.path.join(path, "*.csv")))

dataframes_original = [pd.read_csv(i) for i in all_csv_files_sorted]

dataframes = dataframes_original

dataframes = [i.dropna(axis=1, how='all') for i in dataframes]
dataframes = [i.fillna(0) for i in dataframes]

master_dataframe = pd.concat(dataframes, axis=0)
master_dataframe_cleaned = master_dataframe.dropna(axis=1, how='any')

master_dataframe_cleaned.to_csv('combined_data.csv', index=False )

# %%
s3 = boto3.client('s3')
s3.upload_file('/Users/varghesejacob/Desktop/AiCore/Migration_Project/combined_data.csv', 'my-boto3-bucket-varghese', 'combined_data.csv')
