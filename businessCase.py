"""
BUSINESS CASE
TASK 1

Jakub.Adamowicz@CBRE.com
"""
import pandas as pd
import numpy as np

# -*- coding: utf8 -*-

# Paths to the files needed in TASK 1
file1 = r'C:\Users\jadamowicz\Desktop\test\Table_0.xlsx'
file2 = r'C:\Users\jadamowicz\Desktop\test\Table_1.csv'
file3 = r'C:\Users\jadamowicz\Desktop\test\Table_2.xlsx'

"""
1. Load and merge all files Table_* using pandas package
"""
# Creating DataFrames from the given files
df1 = pd.DataFrame(pd.read_excel(file1, engine='openpyxl'))
df3 = pd.DataFrame(pd.read_excel(file3, engine='openpyxl'))
df2 = pd.DataFrame(pd.read_csv(file2, sep=',', lineterminator='\n', encoding='utf-8'))

df2.replace({r'\r': ''}, regex=True, inplace=True)
df2.rename(columns={'Origin\r': 'Origin'}, inplace=True)
df2["Type"].replace({"?45": "Ź45", "V1?R": "V1ŹR", "V0?P": "V0ŹP"}, inplace=True)


# Joining three DataFrames into one DataFrame
df = df1.append(df2)
df = df.append(df3)
df.reset_index(inplace=True)
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
df[['Acctg Date', 'Date']] = df[['Acctg Date', 'Date']].apply(pd.to_datetime)
df['Days Diff'] = (df['Acctg Date'] - df['Date']).dt.days

"""
6. For each row calculate difference (number of BUSINESS days) between Acctg Date and Date columns
(ignore weekends and UK bank holidays)
"""
# Using numpy busday_count, creation of copied DataFrame to make counting only on rows with column "Dates" filled
df['index1'] = df.index
dfCopy = df.copy()
dfCopy.dropna(subset=['Days Diff'], inplace=True)
dfCopy["Business Days"] = np.busday_count(dfCopy["Date"].dt.date, dfCopy["Acctg Date"].dt.date)

# Adding "Business Days" column to the DataFrame
dfCopy = dfCopy[["index1", "Business Days"]]
df = pd.merge(df, dfCopy, how='left', on="index1")
df.drop(["index1"], axis=1, inplace=True)

"""
7. Convert Amount to PLN using FXrates.csv
"""
convPath = r'C:\Users\jadamowicz\Desktop\test\FXrates.csv'
convFrame = pd.read_csv(convPath, sep=',', lineterminator='\n', index_col='Currency').squeeze()

df = df.merge(convFrame, how='left', left_on='Currency', right_on='Currency')
df['Amount PLN'] = (df['Amount'] / df['Per USD\r']) * convFrame.loc['PLN']
df.drop(columns=['Per USD\r'], inplace=True)

"""
8. Create folder results and save separate file for EACH unique Type value, 
use Type in name of saved file (for example Table_4P4.xlsx)
"""

uniqueTypes = df.Type.unique()
outfolder = r'C:\Users\jadamowicz\Desktop\test\Table_'
for type in uniqueTypes:
    dftype = df.copy()
    dftype.drop(dftype[dftype.Type != type].index, inplace=True)
    writer = pd.ExcelWriter(outfolder + str(type) + ".xlsx", engine='xlsxwriter')
    dftype.to_excel(writer, sheet_name="Audit1", index=False)
    writer.save()
