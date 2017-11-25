#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 23:04:19 2017

@author: jyothsnap
"""

tuple1 = (41,51,61,71)
print(tuple1.index(61))
print(type(tuple1))
map1={'length':10,'weight':20}
len(map1)
map1['height'] =10
map1['width'] = 7
print("length of map: ",len(map1))
map1['height'] = 3
map1.keys()
map1.get('height')
map1.items()
print("map1 : ",map1)
print("map1.items : ",map1.items())

map2 = {'length':[10,20,30],
        'width':[6,7]}
print(map2)
