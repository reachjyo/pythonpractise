#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:55:50 2017

@author: jyothsnap
"""

#practising String

s1= 'SanFrancisco is in United State'
print(s1)
list1 = s1.split()
print("list:",list1.count)
print(list1)
list1[4] = 'States of America'
s2 =''.join(map(str,list1))
print("newString :",s2)
