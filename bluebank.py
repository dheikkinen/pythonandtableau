# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 15:32:15 2023

@author: dheik
"""

import json
import pandas
import numpy
import matplotlib.pyplot

#option 1 to read json data
json_file = open('loan_data_json.json')
data = json.load(json_file)

#option 2 to read json data
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)
    
#transform json to dataframe
loandata = pandas.DataFrame(data)

#finding unique values for purpose column
loandata['purpose'].unique()

#describing the data
loandata.describe()

#describe data for a specific column
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()

#using exp() to get annual income and adding column to dataframe
income = numpy.exp(loandata['log.annual.inc'])
loandata['annual.income'] = income

#working with if statements
a=40
b=500
if b>a:
    print('b is greater than a')
    
#adding more conditions
a=40
b=500
c=1000
if b>a and b<c:
    print('b is greater than a but less than c')
    
#what if a condition is not met
a=40
b=500
c=20
if b>a and b<c:
    print('b is greater than a but less than c')
else:
    print('no conditions met')
  
#another condition, different metrics
a=40
b=0
c=20
if b>a and b<c:
    print('b is greater than a but less than c')
elif b>a and b>c:
    print('b is greater than a and c')
else:
    print('no conditions met')

#using or    
a=40
b=500
c=20
if b>a or b<c:
    print('b is greater than a or less than c')
else:
    print('no conditions met')
    
#fico score
fico = 250

#fico: The FICO credit score of the borrower.
#- 300 - 400: Very Poor
#- 401 - 600: Poor
#- 601 - 660: Fair
#- 661 - 780: Good
#- 781 - 850: Excellent

if fico >= 300 and fico < 401:
    ficocat = 'Very Poor'
elif fico >= 401 and fico < 601:
    ficocat = 'Poor'
elif fico >= 601 and fico < 661:
    ficocat = 'Fair'
elif fico >= 661 and fico < 781:
    ficocat = 'Good'
elif fico >= 781:
    ficocat = 'Excellent'
else:
    ficocat = 'Invalid result'
print(ficocat)
    
#for loops

fruits = ['apple', 'orange', 'banana', 'grape']

for x in fruits:
    print(x)
    y = x + ' fruit'
    print(y)
    
for x in range(0,4):
    y = fruits[x] + ' for sale'
    print(y)
    
#applying for loops to loan data
#using first 10

length = len(loandata)
ficocat = []
for x in range(0,length):
    category = loandata['fico'][x]
    
    try:
        if category >= 300 and category < 401:
            cat = 'Very Poor'
        elif category >= 401 and category < 601:
            cat = 'Poor'
        elif category >= 601 and category < 661:
            cat = 'Fair'    
        elif category >= 661 and category < 781:
            cat = 'Good'
        elif category >= 781:
            cat = 'Excellent'
        else:
            cat = 'Invalid result'  
    except:
        cat = 'Invalid result'
              
    ficocat.append(cat)
    
ficocat = pandas.Series(ficocat)

loandata['fico.category'] = ficocat

#df.loc as conditional statements
#df.loc[df[columnname] condition, newcolumnname] = 'value if condition is met'

#for interest rates, a new column if int rate > 0.12, then high, otherwise low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'
loandata.loc[loandata['int.rate'] <= 0.12, 'int.rate.type'] = 'Low'

#number of loans by fico category

catplot = loandata.groupby(['fico.category']).size()
catplot.plot.bar(color = 'green', width = 0.1)
matplotlib.pyplot.show()

catplotpurpose = loandata.groupby(['purpose']).size()
catplotpurpose.plot.bar(color = 'purple', width = 0.25)
matplotlib.pyplot.show()

#scatter plots
#annual income vs dti correlation

ypoint = loandata['annual.income']
xpoint = loandata['dti']
matplotlib.pyplot.scatter(xpoint,ypoint, color = '#1B1B1B')
matplotlib.pyplot.show()

#writing to csdv
loandata.to_csv('loan_cleaned.csv', index = True)

