# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 11:25:21 2018

@author: yuyao
"""

for x in range (1,20):
    for y in range (1,33):
        z=100-x-y
        if ((5*x+3*y+z/3==100) and (z%3==0)):
            print(x,y,z)
            