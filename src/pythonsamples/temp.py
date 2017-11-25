# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
list1 =[10,30,40,20,60]


list2 =[1,4,5,16,25,36,49]
list2[2]
list2[2] = 27
for e in list1:
    print(e)
#for index,element in enumerate(list2):
 #   print(index,element)
  #  list2.append(list1[index]**3) 
    
list1 = [10,30,20,40,50]
list1.append(60)
print(list1)
list1.extend([70,80])
list1.sort()
list1.insert(1,15)
print(len(list1))
print(list1)    
list3 = [11,21,31,41,51,61,71]
list3[1:5]
print(list3[3:5])
print("latest :",list3[::3])
print(list3[2::])
list3.sort()
print(list3)
print(len(list3))

