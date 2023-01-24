#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 01:35:39 2023

@author: keyur
"""

NumList = ['erg','erg','erg','erg']
DemList = ['erg','erg','erg','erg','erg']

NumListCopy = NumList.copy()
DemListCopy = DemList.copy()
s = 0

for i in range(len(NumList)):
    for j in range(len(DemList)):
        if NumList[i] == DemList[j]:
            DemListCopy.pop(j-s)
            NumListCopy.pop(i-s)
            s += 1
            break

NumList = NumListCopy
DemList = DemListCopy