# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 09:52:36 2025

@author: user
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


veriler= pd.read_csv('sepet.csv', header= None) # header kolon basligi olmadigi icin veriliyor.
t = []
for i in range(0,7501):#7501 satir var hepsini almasini istiyoruz
    t.append([str(veriler.values[i,j]) for j in range (0,20)])
    
from apyori import apriori

kurallar= apriori(t, min_support= 0.01, min_confidence= 0.2, min_left= 3, min_lenght= 2)
print(list(kurallar))


