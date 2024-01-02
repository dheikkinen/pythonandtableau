# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 13:56:22 2023

@author: dheik
"""

import pandas
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

#reading xlsx files
data = pandas.read_excel('articles.xlsx')

#get summary of data
data.describe()

#get summary of clumns
data.info()

#counting the number of articles per source
#format of groupby: df.groupby(['column_to_group']['column_to_count']).count()

data.groupby(['source_id'])['article_id'].count()

#number of reactions by publisher
data.groupby(['source_id'])['engagement_reaction_count'].sum()

#drop engagement plugin column
data = data.drop('engagement_comment_plugin_count', axis=1)

#functions in python
def thisFunction():
    print('This is a function')
    
thisFunction()

#This is a function with variables

def aboutMe(name, surname, location):
    print('This is ' + name + ', my surname is ' + surname + ". I am from " + location) 
    return name, surname, location

a = aboutMe('Dave', 'Heikkinen', 'Detroit')

#Using for loops in a function

def favfood(food):
    for x in food:
        print('Top food is ' + x)
    
    
fastfood = ['burgers', 'fries', 'ice cream', 'pizza']

favfood(fastfood)

#Creating a keyword flag
keyword = "crash"

#creating a for loop to isolate each title

# length = len(data)
# keyword_flag = []
# for x in range(0,length):
#     heading = data['title'][x]
#     if keyword in heading:
#         flag = 1
#     else:
#         flag = 0
#     keyword_flag.append(flag)
        
#creating a function

def keywordflag(keyword):
    length = len(data)
    keyword_flag = []
    for x in range(0,length):
        heading = data['title'][x]
        try:
            if keyword in heading:
                flag = 1
            else:
                flag = 0
        except:
            flag = 0
        keyword_flag.append(flag)
    return keyword_flag
        
keywordflag = keywordflag('murder')
        
#Creating a new column in dataframe

data['keyword_flag'] = pandas.Series(keywordflag)
 
#SentimentIntensityAnalyzer
sent_int = SentimentIntensityAnalyzer()

text = data['title'][45]
sent = sent_int.polarity_scores(text)

neg = sent['neg']
pos = sent['pos']
neu = sent['neu']

#adding a for loop to extract sentiment per title

title_neg_sent = []
title_pos_sent = []
title_neu_sent = []

length = len(data)

for x in range(0,length):
    try:
        text = data['title'][x]
        sent_int = SentimentIntensityAnalyzer()
        sent = sent_int.polarity_scores(text)
        neg = sent['neg']
        pos = sent['pos']
        neu = sent['neu']
    except:
        neg = 0
        pos = 0
        neu = 0
    title_neg_sent.append(neg)
    title_pos_sent.append(pos)
    title_neu_sent.append(neu)
  
title_neg_sent = pandas.Series(title_neg_sent)
title_pos_sent = pandas.Series(title_pos_sent)
title_neu_sent = pandas.Series(title_neu_sent)
    
data['title_neg_sent'] = title_neg_sent
data['title_pos_sent'] = title_pos_sent
data['title_neu_sent'] = title_neu_sent
    
#writing data to xlsx file
data.to_excel('blogme_clean.xlsx', sheet_name = 'blogmedata', index = False)
