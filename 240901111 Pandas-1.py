#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
#Empty DataFrame
df=pd.DataFrame()
print(df)


# In[15]:


emp=pd.Series(['Parker','John','Smith','William'])
id=pd.Series([102,107,109,114])
frame={'Emp':emp,'ID':id}
result=pd.DataFrame(frame)
print("\nSeries to Data Frame\n")
print(result)


# In[14]:


print("\n Extracting one column:\n")
print(result['Emp'])


# In[13]:


print("\nAdding new column:\n")
result['Age']=pd.Series([35,24,40,38])
print(result)


# In[12]:


print("\nDeleting one column:\n")
del result['Age']
print(result)


# In[18]:


print("\nSice rows:\n",result[1:3])


# In[24]:


d2 = pd.DataFrame([['Dale', 123], ['Mark', 143]], columns = ['Emp', 'ID'])
print("\nAdding new row values:\n",result.append(d2))


# In[ ]:




