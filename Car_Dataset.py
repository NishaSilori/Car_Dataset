#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


car = pd.read_csv(r'D:\python docouments\analytics_dataset\2. Cars Data1.csv')


# In[3]:


car.isnull().sum()


# In[4]:


car['Cylinders'].fillna(car['Cylinders'].mean(), inplace = True)


# In[5]:


car.head(2)


# ## Check what are the different type of make are there in our dataset and what is the count (Occurence) of each make in the data?

# In[6]:


car.head(2)


# In[7]:


car['Make'].value_counts()


# ## Show all the records where origin is Asia or Europe

# In[8]:


car.head(2)


# In[9]:


car[car['Origin'].isin(['Asia', 'Europe'])]


# ## Remove all the records (rows) where weight is above 4000.

# In[10]:


car.head(2)


# In[11]:


car[~car['Weight'] > 4000]


# ## Increase the value of 'MPG_City' column by 3

# In[12]:


car['MPG_City'] = car['MPG_City'].apply(lambda x:x+3)


# In[13]:


car


# In[ ]:




