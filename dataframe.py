#!/usr/bin/env python
# coding: utf-8

import pandas as pd

df1 = pd.DataFrame(columns=["Textiles","CO2e"])

textile_data = {'Synthetic': 14.0,'Cotton': 9.5,'Hemp': 4.0,'Wool': 7.0,'Viscose': 11.0,'Linen': 2.0}
i=0
for textile in textile_data:
    df1.loc[i] = [textile, textile_data[textile]]
    i=i+1

def get_co2 (textile):
    value = df1.get(df1["Textiles"] == textile)
    return value.at[0,"CO2e"]

def calculation(text_dict, textile_data):
    n = len(text_dict)
    overall_co2 = 0
    for all in text_dict:
        co2_textile = get_co2(all)
        textile_perc = text_dict[all]
        overall_co2 += co2_textile * (textile_perc)/100
    return overall_co2
    





