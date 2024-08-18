#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_excel("D:\ASR.xlsx")


# In[3]:


df.shape


# In[4]:


df.head(10)


# In[5]:


df.info()


# In[6]:





# In[7]:


#drop unrelated/blank columns
df.drop(['New','PendingS'], axis=1, inplace=True)


# In[9]:


# checking null values
# sum will give total values of null values
pd.isnull(df).sum()


# In[10]:


df.shape


# In[11]:


#drop null values
df.dropna(inplace=True)


# In[12]:


df.shape


# In[13]:


#change data type
df['ship-postal-code']=df['ship-postal-code'].astype('int')


# In[14]:


#checking whelther the data type change or not
df['ship-postal-code'].dtype


# In[15]:


df['Date']=pd.to_datetime(df['Date'])


# In[16]:


df.info()


# In[17]:


#describe() method return description of the data in the Dataframe(i.e count,mean,std,min.etc)
df.describe()


# In[18]:


#use describe() for specific columns
df[['Qty','Amount']].describe()


# # Exploratory Data Analysis
# 

# In[19]:


df.columns


# In[21]:


ax=sns.countplot(x='Size' , data=df)
for bar in ax.containers:
    ax.bar_label(bar)


# Note:- From the above Graph you can observe that most of the people buys M-size

# # Group By :-
# The groupby() function in pandas is used to group data based on one or more columns in Dataframe
# 

# In[23]:


S_Qty=df.groupby(['Size'], as_index=False)['Qty'].sum().sort_values(by='Qty',ascending=False)

ax = sns.barplot(x='Size',y='Qty', data=S_Qty)
for container in ax.containers:
    ax.bar_label(container)


# Note:-From the above Graph you can observe that most of the Quantity buys M-size in the sales

# In[24]:


plt.figure(figsize=(10,5))

ax=sns.countplot(data=df, x='Courier Status',hue= 'Status')
for container in ax.containers:
    ax.bar_label(container)
plt.show()


# Note:-From the above Graph you can observe that most of the order are shipped through courier

# In[25]:


df['Category'] = df['Category'].astype(str)
column_data = df['Category']
data = column_data
# counts, edges, bars = plt.hist(data)
plt.figure(figsize=(10,5))
counts, edges, bars= plt.hist(column_data, bins=10, edgecolor='Black')
plt.xticks(rotation=90)
plt.bar_label(bars)
plt.show()


# Note:- From the Graph you can observe that most of the buyers buys T-shirt

# In[26]:


#Checking B2B Data by using pie chart
B2B_Check = df['B2B'].value_counts()

# Plot the Pie chart
plt.pie(B2B_Check, labels=B2B_Check.index ,autopct='%1.1f%%')
#plt.axis('equals')
plt.show()


# Note: From above chart we can see that maximum i.e. 99.3% of buyers are retailers and 0.8% are B2B buyers

# In[27]:


# Prepare data for scatter plot
x_data = df['Category']
y_data = df['Size']

# Plot the scatter plot
plt.scatter(x_data, y_data)
plt.xlabel('Category')
plt.ylabel('Size')
plt.title('Scatter Plot')
plt.show()


# In[28]:


#plot count of cities by state
plt.figure(figsize=(12,6))
ax = sns.countplot(data=df,x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=90)

for container in ax.containers:
    ax.bar_label(container,)
plt.show()


# In[29]:


#top_10_States
top_10_state = df['ship-state'].value_counts().head(10)
# Plot count of cities by State
plt.figure(figsize=(12,6))
ax = sns.countplot(data=df[df['ship-state'].isin(top_10_state.index)],x='ship-state')
plt.xlabel('ship-state')
plt.ylabel('count')
plt.title('Distribution of State')
plt.xticks(rotation=45)
for container in ax.containers:
    ax.bar_label(container)
plt.show()


# Note: From above you can see that most of the buyers are from Maharashtra state

# # Conclusion:-
# 

# The Data Analysis reveals that the business has a significant customer base in Maharashtra state,mainly serves retailers, fulfills orders through Amazon, experience high demand for T-shirts, and sees M-Size as the preferred choice among buyers.

# In[ ]:




