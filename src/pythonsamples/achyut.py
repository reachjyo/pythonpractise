#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 07:19:50 2017

@author: jyothsnap
"""
import pandas as pd

url1 = 'https://raw.githubusercontent.com/studyml-lab/Python-Basics/master/train_kaggle.csv'
#titanicdata = pd.read_csv(url1)
map1 = {'Name' : ['ram','jyo','sandy'],
        'height' : [6,7,8],
        'weight' : [5,6,7]}
titanicdata = pd.DataFrame(map1)


print(titanicdata[[ 'Name', 'height']])
titanicdata['Pclass1'] = 2
#print(list2)
print(titanicdata[[ 'Name', 'Pclass1']])
print(titanicdata.columns)
print(titanicdata.shape)
print(titanicdata.iloc[:,:])
print(titanicdata.iloc[0:3,0:3])
print("-------------------------iloc--------------------------------------------")
print(titanicdata.iloc[:,:])
#print("-------------------width--------------------------------------------------")

#print(titanicdata.loc[0:2,'width'])
print("------------------------loc---------------------------------------------")

print(titanicdata.loc[0:2,'height'])
