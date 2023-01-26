#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:01:17 2023

@author: keyur
"""
import UnitModule as um

Ivalue = int(input('What is the value of the unit you want to change? '))
Iunit = input('What are the units you want to put in? (Put in your units in square brackets like [m]/[s] or [J]*[s]) ') #Is the input variable for the unit that needs to be converted.

conv, Unit = um.SItoCGS(Iunit)
Nvalue = Ivalue*conv
        
print('The new value in cgs units is '+str(Nvalue)+' '+Unit)