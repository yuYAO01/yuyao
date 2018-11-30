# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 08:54:28 2018

@author: yuyao
"""

import random
import string
n=1
a=list(range(1,200))
for n in a:
    b=''.join(random.sample(string.ascii_letters + string.digits, 18))
    n=n+1
    print(b)