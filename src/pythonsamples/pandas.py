#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 10:33:39 2017

@author: jyothsnap
"""

import pandas as pd
dict ={
       "country": ["Brazil","Russia","India","China","South Africa"],
       "capital":["Brasili","Moscos","New Delhi","Beijeng","Pretoria"],
       "area":[8.516,17.10,3.286,9.597,1.221],
       "population":[200.4,143.5,1252,1357,52.98]
       }

print("before :",dict)
brics = pd.DataFrame(dict)
print("brics : ",brics)
print("length of brics :", len(brics))
print("type of brics: ",type(brics))
print("shape :", brics.shape)
print("columns: ",brics.columns)
print("datatype : ",brics.dtypes)
brics.index =["BR","RU","IN","CH","SA"]
print("brics : ",brics)
print("brics.info :",brics.info)
print("printing first 2 rows :",brics.head(2))
print("printing last 2 rows :",brics.tail(2))
brics.to_csv("/users/jyothsnap/brics.csv")
print("brics befire converting to DataFrame :",brics)
bricsDF =pd.read_csv("/users/jyothsnap/brics.csv",index_col=0)
print("bricsDF :  ",bricsDF)
print("series :",bricsDF['country'])
print("Data Frame :",bricsDF[['country']])
print(type(brics[["country"]]))
print(type(brics["country"]))


