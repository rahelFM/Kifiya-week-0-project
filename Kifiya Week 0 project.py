#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
df_benin = pd.read_csv(r'C:\Users\Rahel\Desktop\kifiya\data\data\benin-malanville.csv')
df_sierra_leone = pd.read_csv(r'C:\Users\Rahel\Desktop\kifiya\data\data\sierraleone-bumbuna.csv')
df_togo = pd.read_csv(r'C:\Users\Rahel\Desktop\kifiya\data\data\togo-dapaong_qc.csv')

df_benin['Country'] = 'Benin'
df_sierra_leone['Country'] = 'Sierra Leone'
df_togo['Country'] = 'Togo'

df = pd.concat([df_benin, df_sierra_leone, df_togo], ignore_index=True)

print(df.head())

