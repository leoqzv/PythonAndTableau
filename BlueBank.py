# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 22:04:51 2022

@author: leola
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



#method 1 to read JSON data

json_file  = open("loan_data_json.json")
data = json.load(json_file)

#Method 2 
with open("loan_data_json.json") as json_file:
    data=json.load(json_file)
    print(data)
    


fruit = ['apple', 'lemon','pear']

fruit.append('cherry')
fruit.insert(0, 'lime')

fruit.append('pasta')
fruit.pop()

mydict = {
    'location': 'USA',
    'name':'Jim',
    'lucky number': 1,}

mydict.keys()
mydict.values()
mydict.items()

mydict['city'] = 'Philadelphia'

mydict.items()

loandata = pd.DataFrame(data)

#find unique values

loandata['purpose'].unique()

loandata.describe()

loandata['fico'].describe()

loandata['dti'].describe()

#using exp to get income

income = np.exp(loandata['log.annual.inc'])

loandata['annualincome'] = income

arr = np.array([1,2,3,4])

#If statement


a = 40
b = 5000
if a < b:
    print("b is greater than a")

# fico >= 300 and < 400:
# 'Very Poor'
# fico >= 400 and ficoscore < 600:
# 'Poor'
# fico >= 601 and ficoscore < 660:
# 'Fair'
# fico >= 660 and ficoscore < 780:
# 'Good'
# fico >=780:
# 'Excellent'
length = len(loandata)
ficocat = []
for x in range(0,length):
    category  = loandata['fico'][x]
    
  #Try and except  
    try:
        if category < 400:
            cat = 'Very poor'
        elif  category<600:
            cat = "Poor"
        elif category < 660:
            cat = 'Fair'
        elif  category <700:
            cat = "Good"
        elif  category >=700:
            cat = "Excellent"
        else:
            cat = "Unknown"
    except:
        cat= "Unknown"        
    print(category)
    print(cat)
    ficocat.append(cat)
 
ficocat   = pd.Series(ficocat)
loandata['fico.category'] = ficocat
 



loandata.loc[loandata['int.rate']>0.12,'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate']<=0.12,'int.rate.type'] = 'Low'

#number of loans/rows by fico.category

catplot = loandata.groupby(['fico.category']).size()
purposeplot = loandata.groupby(['purpose']).size()



catplot.plot.bar(color='green',width=0.1)
plt.show()

purposeplot.plot.bar(color='black',width=0.5)
plt.show()

#scatter plots

ypoint = loandata['annualincome']
xpoint = loandata['dti']
plt.scatter(xpoint, ypoint, color ='#000000')
plt.show()


# writing to csv

loandata.to_csv('loan_cleaned.csv', index=True)