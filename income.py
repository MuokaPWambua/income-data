#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 07:06:42 2022

@author: kali
"""
import matplotlib.pyplot as plt
import numpy as np

income = np.random.normal(27000, 15000, 10000)

mean = np.mean(income)
median = np.median(income)

 
print(f'mean: {mean}, median: {median}')

plt.hist(income, 50)
plt.show()