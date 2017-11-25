#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 21:43:15 2017

@author: jyothsnap
"""

import pandas as pd

map1 = {'length' : [10,20,30],
        'height' : [6,7,8],
        'width' : [5,6,7]}
df1 = pd.DataFrame(map1)
print(df1)

url1 = 'https://raw.githubusercontent.com/studyml-lab/Python-Basics/master/train_kaggle.csv'
titanicdata = pd.read_csv(url1)

type(titanicdata)
titanicdata.shape
length = len(titanicdata)
print(length)
titanicdata.info()
print("datatypes" ,titanicdata.dtypes)
titanicdata.columns
titanicdata.head(5)
titanicdata.tail(5)

# accessing columns
titanicdata[['Name','Pclass']]
titanicdata['Pclass1'] = 2
titanicdata['Pclass'] = 2

# accessing rows
titanicdata.iloc[0]
titanicdata.iloc[1]
titanicdata.iloc[0:3]
#accessing rows and columns
titanicdata.iloc[0:3,3]
titanicdata.loc[0:4,'Name']
titanicdata.loc[5:]
titanicdata.loc[:5]

# 
titanicdata.loc[titanicdata.Sex =='female',['Name','Pclass']]
titanicdata.info()
titanicdata.loc[titanicdata['Age'].isnull() == True,'Name']
titanicdata.loc[(titanicdata.Sex =='female') & (titanicdata.Age >50),['Name','Pclass'] ]
titanicdata1 = titanicdata.drop(['Pclass1'],axis=1,inplace = False)

#Concat two frames

t3 =pd.concat([titanicdata,titanicdata1])
t3.shape
t3.to_csv('/users/jyothsnap/newfile.csv')