# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 13:34:44 2020

@author: ~Chrys 楊筑云~
"""

import random

num = random.randrange(1, 2)

try:
    rand = int(input("請輸入數字："))
    if num == rand:
        print("答對了")

except:
    print("請輸入整數")
    
else:
    print("try again")