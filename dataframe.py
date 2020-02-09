#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
pandas.__version__


# In[14]:


df1 = pd.DataFrame(columns=["Textiles","CO2e"])

textile_data = {'Synthetic': 14.0,'Cotton': 9.5,'Hemp': 4.0,'Wool': 7.0,'Viscose': 11.0,'Linen': 2.0}
i=0
for textile in textile_data:
    df1.loc[i] = [textile, textile_data[textile]]
    i=i+1


# In[15]:


print(df1)


# In[17]:


test = 'Synthetic'


# In[18]:


df1["CO2e"].where(df1["Textiles"] == test)


# In[42]:


value = df1.get(df1["Textiles"] == test)


# In[44]:


value.at[0,"CO2e"]


# In[ ]:




