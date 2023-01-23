#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 22:01:17 2023

@author: keyur
"""
import UnitModule as um

Iunit = input('What are the units you want to put in? (Put in your units in square brackets like [m]/[s] or [J]*[s]) ') #Is later going to be an input variable

conv = um.SItoCGS(Iunit)
        
print(conv)