#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 01:35:39 2023

@author: keyur
"""

NumList = ['erg','erg','erg','erg']
DemList = ['erg','erg','erg','erg','erg']

lendiff=len(DemList)-len(NumList)

if lendiff>0:
    for i in range(lendiff):
        NumList.append(0)
elif lendiff<0:
    for i in range(abs(lendiff)):
        DemList.append(0)

i=0
ireset=False
while i<len(NumList):
    if ireset==True:
        i=0
    j=0
    while j<len(DemList):
        if NumList[i] == DemList[j]:
            DemList.pop(j)
            NumList.pop(i)
            ireset=True
        j+=1
    i+=1

zeroinlist=True
while zeroinlist==True:
    print(NumList)
    if 0 in NumList:
        NumList.remove(0)
    elif 0 in DemList:
        DemList.remove(0)
    else:
        zeroinlist=False
