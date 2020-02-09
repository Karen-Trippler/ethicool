#!/usr/bin/python3

#gets the html text from the passed in website
def get_soup(url):
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    type(soup)
    return soup

#function that extracts the material string
def get_material(soup):
    #finds all div tags in the whole html document
    all_divs = soup.find_all('div')
    tag_list = []

    #loops through all divs to find the relevant ones
    for div in all_divs:
        
        #searches for the relevant class description
        div = str(div)
        div_object = re.search("class=\"product-details__care\"",div)
        
        
        if div_object:
            #selects from the start of the tag till 100 characters further down
            class_tag = div[div_object.start():div_object.start()+100]
            #adds them to a list
            tag_list.append(class_tag)
        
            #selects the first found tag
            desig_tag = tag_list[0]
            
            #extracts the material string based on specific tags
            material = desig_tag.split("<p>")[1].split(".<br/>")[0]
            return material

#function getting a dictionary from the textile string
def get_textile(material):
    whole_mat = material.split(' ')

    text_dict = {}

    for value in whole_mat:
        if value.find('%')>0:
            percent_index = whole_mat.index(value)
            text_name = whole_mat[percent_index+1].replace(',', '').strip().lower()
            text_percent = whole_mat[percent_index].replace('%','')
            text_dict[text_name] = text_percent
    return text_dict


import pandas as pd
#Import statements
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

def get_co2 (textile):
	df1 = pd.DataFrame(columns=["Textiles","CO2e"])
	textile_data = {'Synthetic': 14.0,'Cotton': 9.5,'Hemp': 4.0,'Wool': 7.0,'Viscose': 11.0,'Linen': 2.0}
	i=0
	for textile in textile_data:
		df1.loc[i] = [textile, textile_data[textile]]
		i=i+1
		value = df1.get(df1["Textiles"] == textile)
	return value.at[0,"CO2e"]

def calculation(text_dict):
    n = len(text_dict)
    overall_co2 = 0
    for all in text_dict:
    	co2_textile = get_co2(all.upper())
    	textile_perc = text_dict[all]
    	overall_co2 += co2_textile * (textile_perc)/100
    return overall_co2