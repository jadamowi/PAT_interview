"""
BUSINESS CASE
TASK 1
"""
import pandas as pd
import numpy as np

# -*- coding: utf8 -*-

# Paths to the files needed in TASK 1
file1 = r'C:\Users\jakub\PAT_interview\Table_0.xlsx'
file2 = r'C:\Users\jakub\PAT_interview\Table_1.csv'
file3 = r'C:\Users\jakub\PAT_interview\Table_2.xlsx'

"""
1. Load and merge all files Table_* using pandas package
"""
# Creating DataFrames from the given files
df1 = pd.read_excel(file1, engine='openpyxl')
df3 = pd.read_excel(file3, engine='openpyxl')
df2 = pd.read_csv(file2, sep=',', lineterminator='\n', encoding='utf-8')

df2.replace({r'\r': ''}, regex=True, inplace=True)
df2.rename(columns={'Origin\r': 'Origin'}, inplace=True)
df2["Type"].replace({"?45": "Ź45", "V1?R": "V1ŹR", "V0?P": "V0ŹP"}, inplace=True)


# Joining three DataFrames into one DataFrame
to_concat = [df1, df2, df3]
df = pd.concat(to_concat)

"""
2. Drop duplicates if any appear in data
"""
df.drop_duplicates(inplace=True)

"""
3. Show (for example print) number of null values in each column
"""
print(df.isnull().sum())

"""
4. Fill numerical null values with 1337
"""
df['Func Unit'].fillna(1337, inplace=True)

"""
5. For each row calculate difference (number of days) between Acctg Date and Date columns
"""
# Convertion of date columns into DateTime and counting difference in days
df['Acctg Date'] = pd.to_datetime(df['Acctg Date'])
df['Date'] = pd.to_datetime(df['Date'])
df['Days Diff'] = (df['Acctg Date'] - df['Date']).dt.days

"""
6. For each row calculate difference (number of BUSINESS days) between Acctg Date and Date columns
(ignore weekends and UK bank holidays)
"""

def business_days(start, end):
    mask = pd.notnull(start) & pd.notnull(end)
    start = start.values.astype('datetime64[D]')[mask]
    end = end.values.astype('datetime64[D]')[mask]
    result = np.empty(len(mask), dtype=float)
    result[mask] = np.busday_count(start, end)
    result[~mask] = np.nan
    return result

df["Business Days"] = business_days(df['Acctg Date'], df['Date'])

"""
7. Convert Amount to PLN using FXrates.csv
"""
conv_path = r'C:\Users\jakub\PAT_interview\FXrates.csv'
conv_frame = pd.read_csv(conv_path, sep=',', lineterminator='\n', index_col='Currency').squeeze()

df = df.merge(conv_frame, how='left', left_on='Currency', right_on='Currency')
df['Amount PLN'] = (df['Amount'] / df['Per USD\r']) * conv_frame.loc['PLN']
df.drop(columns=['Per USD\r'], inplace=True)

"""
8. Create folder results and save separate file for EACH unique Type value, 
use Type in name of saved file (for example Table_4P4.xlsx)
"""

unique_types = df.Type.unique()
out_folder = r'C:\Users\jakub\PAT_interview\Table_'
for type in unique_types:
    temp = df.loc[df.Type == type]
    file_name = f'{out_folder}{type}.xlsx'
    temp.to_excel(file_name, index=False)


