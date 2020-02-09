#!/usr/bin/env python
# coding: utf-8

import pandas as pd

df1 = pd.DataFrame(columns=["Textiles","CO2e"])

textile_data = {'Synthetic': 14.0,'Cotton': 9.5,'Hemp': 4.0,'Wool': 7.0,'Viscose': 11.0,'Linen': 2.0}
i=0
for textile in textile_data:
    df1.loc[i] = [textile, textile_data[textile]]
    i=i+1

test = 'Synthetic'

value = df1.get(df1["Textiles"] == test)

value.at[0,"CO2e"]

def calculation(text_dict, textile_data):
    n = number of elements in the dictionary
    loop over all elements
    cotton : 98
        calculation
        return calculated value
    





