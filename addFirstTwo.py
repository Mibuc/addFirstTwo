#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 13:34:43 2019

@author: Michael
"""
#%%
import pdb

def addFirstTwo(l):
    # pdb.set_trace()
    try:
        return l[0] + l[1]
    except IndexError:
        print("List needs to be greater or equal to two.")