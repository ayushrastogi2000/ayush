# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 01:01:14 2017

@author: 
"""

import pandas as pd

df = pd.read_csv('stopwords.csv' , header=None , names=["Urls"])
filename = open('stopwords1.csv', 'a')
df.to_csv(filename, sep='\t', encoding='utf-8')

