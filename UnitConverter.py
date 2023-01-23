#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:01:17 2023

@author: keyur
"""

Iunit = input('What are the units you want to put in? (Put in your units in square brackets like [m]/[s] or [J]*[s]) ') #Is later going to be an input variable

#Bolean values for the loop
Div = False
Add = False

#The variable for the convertion value for cgs
conv = 1 

#Loop that calculates the convertion value
for i in Iunit:
    
    if i == '[':
        Add = True
    elif i == 'm':
        if Add == True:
            if Div == False:
                conv *= 1e3
            elif Div == True:
                conv /= 1e3
        else:
            continue
    elif i == 's':
        continue
    elif i == ']':
        Add = False
    elif i == '/':
        Div = True
        
print(conv)