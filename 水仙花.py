# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:40:43 2018

@author: yuyao
"""

        for i in range(1,10):
            for j in range(0,10):
                for k in range(0,10):
                    if i*100+j*10+k==i*i*i+j*j*j+k*k*k:
                        print(i*100+j*10+k)
                        for i in range(100,1000):
                            sum=0
                            temp=i
                            while temp:
                                sum=sum+(temp%10)**3
                                temp//=10
                                if sum==i:
                                    print(i)