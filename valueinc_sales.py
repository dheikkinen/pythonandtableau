# -*- coding: utf-8 -*-
'''
Created on Tue Dec 26 23:05:49 2023

@author: dheik
'''

import pandas

#file_name = pandas.read_csv('file.csv') :: format of read_csv

data = pandas.read_csv('transaction.csv')

data = pandas.read_csv('transaction.csv',sep = ';')

#summary of the data
data.info()

#calculating

#defining variables

costPerItem = 11.73
sellingPricePerItem = 21.11
numOfItemsPurchased = 6

#math on Tableau

profitPerItem = sellingPricePerItem - costPerItem
profitPerTransaction = numOfItemsPurchased * profitPerItem
costPerTransaction = numOfItemsPurchased * costPerItem
sellingPricePerTransaction = numOfItemsPurchased * sellingPricePerItem

#costPerTransaction Column calc

#costPerTransaction = costPerItem * numberOfItemsPurchased
#variable = dataFrame['column_name']

costPerItem = data['CostPerItem']
numOfItemsPurchased = data['NumberOfItemsPurchased']
costPerTransaction = costPerItem * numOfItemsPurchased

#adding new column to dataframe

data['CostPerTransaction'] = costPerTransaction

#adding sales per transaction column

data['SalesPerTransaction'] = data['NumberOfItemsPurchased'] * data['SellingPricePerItem']

#adding profit per transaction column

data['ProfitPerTransaction'] = data['SalesPerTransaction'] - data['CostPerTransaction']

#adding markup column ((sales-cost)/cost)

data['Markup'] = (data['ProfitPerTransaction'])/data['CostPerTransaction']

#rounding markup

roundmarkup = round(data['Markup'],2)

data['Markup'] = roundmarkup

myName = 'Dave' + 'Heikkinen'
myDate = 'Day' + '-' + 'Month' + 'Year'

myDate = data['Day']

#checking columns data type
print(data['Day'].dtype)

#change column types

day = data['Day'].astype(str)
year = data['Year'].astype(str)
print(day.dtype)
print(year.dtype)
myDate = day + '-' + data['Month'] + '-' + year

data['Date'] = myDate

#using iloc to view specific columns/rows

data.iloc[0] #views row with index = 0
data.iloc[0:3] #brings in first 3 rows
data.iloc[-5:] #brings in last 5 rows

data.head(5) #brings in first 5 rows

data.iloc[:,2] #all rows, 2nd column

data.iloc[4,2] #4th row, 2nd column

#using split to split client_keywords field
#new_var = column.str.split('sep',expand = True)

split_col = data['ClientKeywords'].str.split(',',expand = True)

#creating new columns for the columns we plit out from ClientKetyword

data['ClientAge'] = split_col[0]
data['ClientType'] = split_col[1]
data['LengthOfContract'] = split_col[2]

#using replace function to remove brackets from string

data['ClientAge'] = data['ClientAge'].str.replace('[','')
data['LengthOfContract'] = data['LengthOfContract'].str.replace(']','')

#change upper case to lower case for item description

data['ItemDescription'] = data['ItemDescription'].str.lower()

#how to merge files

#bringing in new dataset

seasonsData = pandas.read_csv('value_inc_seasons.csv', sep = ';')

#merging files: merge_df = pandas.merge(df_old, df_new, on = 'key')

data = pandas.merge(data, seasonsData, on = 'Month')

#dropping columns: df = df.drop('columnname', axis = 1)

data = data.drop('ClientKeywords', axis = 1)
data = data.drop('Day', axis = 1)
data = data.drop(['Year','Month'], axis = 1)

#exporting into csv for Tableau

data.to_csv('ValueInc_Cleaned.csv', index = False)
