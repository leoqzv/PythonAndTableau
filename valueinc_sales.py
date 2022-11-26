# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 19:11:19 2022

@author: leola
"""

import pandas as pd

#file_name = pd.read_csv("file.csv") <---- format

data = pd.read_csv("transaction.csv")

data = pd.read_csv("transaction.csv" ,sep=";")

#summary of the data
data.info()


#working with calculation
# Defining Variables

#costperitem = 11.73

#sellingpriceperitem = 21.11
#numberofitemspurchased = 6

#matematical operations 

#profifperitem = 21.11 -11.73


costperitem = data["CostPerItem"]
NumberOfItemsPurchased = data["NumberOfItemsPurchased"]

costpertransaction = NumberOfItemsPurchased*costperitem

#adding column to dataframe

data["costpertransaction"] = costpertransaction

#Sales per tranasaciotn


data["SalesPerTransaction"] = data["SellingPricePerItem"] *data["NumberOfItemsPurchased"]


data["ProfitPerTransaction"] = data["SalesPerTransaction"] - data["costpertransaction"]

data["Markup"] =( data["SalesPerTransaction"] - data["costpertransaction"])/data["costpertransaction"]

data["Markup"] = round(data["Markup"], 2)

#combining data fields

my_date = data["Day"].astype(str)+"-"+data["Month"]+"-"+data["Year"].astype(str)

data["my_date"] = my_date

#use iloc to viewspefic columns/row

data.iloc[0]

#new_var = colum.str.split('sep',expand=True)

split_col = data['ClientKeywords'].str.split(',', expand=True)

#create new columns
data['ClientAge']=split_col[0]
data['ClientType']=split_col[1]
data['LengthofContract']=split_col[2]
#use the replace function

data['ClientAge'] = data['ClientAge'].str.replace('[','')

data['LengthofContract'] = data['LengthofContract'].str.replace(']','')

#use lower function
data['ItemDescription'] = data['ItemDescription'].str.lower()

# Merge files
# Bring in a new dataset




seasons = pd.read_csv("value_inc_seasons.csv" ,sep=";")


# merge files: merge_df = pd.merge(df_old, df_new, on = 'key')

data = pd.merge(data, seasons, on = 'Month')

#dropping columns
data = data.drop('Day', axis= 1)

data = data.drop(['Year','Month'], axis= 1)

#export to csv

data.to_csv('ValueInc_Cleaned.csv', index=False)