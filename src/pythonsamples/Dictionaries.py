#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:15:40 2017

@author: jyothsnap
"""

# Definition of countries and capital
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# From string in countries and capitals, create dictionary europe
europe = {
        'spain':'madrid',
        'france':'paris',
        'germany':'berlin',
        'norway':'oslo'
        }

# Print europe
print(europe)
print("printint Items : ",europe.items())
print("printing keys :",europe.keys())
print("printing Values:",europe.values())
print("printing language for country spain :",europe.get('spain'))

x = 10 
y = 1
print(id(x))
print(id(y))
print(id(x) == id(y))
x= y
print(id(x))
print(id(y))
print(id(x) == id(y))
y = y + 4
print(id(x))
print(id(y))
print(id(x) == id(y))
europe['russia'] = 'mosco'
print(europe.items())
europe['test'] = 'test'
print(europe.items())
del(europe['test'])
print(europe.items())
print('spain' in europe)
print('test' in europe)

# Dictionary of dictionaries
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital' :'rome','population':59.83 }

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)