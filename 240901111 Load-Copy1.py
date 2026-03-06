#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
d = pd.read_csv("D:\\employees details.csv")
print(d)


# In[11]:


#Get the column heading
df=pd.DataFrame(d)
print("Columns",df.columns)


# In[13]:


#Get the shape- (no.of rows, no, of columns)
print(df.shape)


# In[15]:


#Get the column heading
df=pd.DataFrame(d)
print("Columns", df.columns)


# In[21]:


df = pd.DataFrame(d)
print("Rows:", df.shape[0])


# In[24]:


print("Last Name",df['Last Name'])


# In[25]:


#Extract/slice the table values- [including this row, excluding this row]
print(df[5:9])


# In[26]:


#Get the particular row values-through row number identification
print("Particular person details",df.loc[10])


# In[27]:


#Get the particular row values- through 'Salary' identification 
print(d.loc[d['Salary']==101004])


# In[30]:


df=d['Salary']/5
print("\nMake an average of total salary:\m",df)


# In[34]:


# Make an average of total marks
df = d['Salary'] / 5
print("\nMake an average of total salary:\n", df)


# In[ ]:




