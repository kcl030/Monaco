# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 14:21:53 2020

@author: Iris
"""
from collections import Counter

def list_difference(a, b):
    count = Counter(a) # count items in a
    count.subtract(b)  # subtract items that are in b
    diff = []
    for x in a:
        if count[x] > 0:
           count[x] -= 1
           diff.append(x)
    return diff


#new vs old
print(list_difference("z y z x v x y x u  ".split(), "x y z w z a a a a".split()))