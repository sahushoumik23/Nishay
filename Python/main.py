#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pa
from sklearn.linear_model import LinearRegression
import numpy as np
import joblib


# In[2]:


data=pa.read_csv('Salary_Data.csv')
inpu=pa.read_csv('hello.csv')


# In[3]:


x=data['YearsExperience']
y=data['Salary']


# In[4]:


x=data['YearsExperience']


# In[5]:


X=x.values.reshape(30,1)
y=data['Salary']


# In[7]:


mind=LinearRegression()


# In[8]:


mind.fit(X,y)


# In[10]:

year=inpu['Years of Experience'][0]
salary=(int)(mind.predict([[year]])[0])






# In[ ]:




