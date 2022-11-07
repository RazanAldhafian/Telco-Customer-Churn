#!/usr/bin/env python
# coding: utf-8

# In[900]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')

Telco_churn = pd.read_csv('/Users/razan/Desktop/Assignment2/Telco-Customer-Churn.csv')
Telco_churn.shape


# In[901]:


Telco_churn.head()


#  # A1) a: --- As you can see there are (7045 Rows × 21 Columns) ---

# In[902]:


Telco_churn.describe()


# In[903]:


Telco_churn.describe(include=['O'])


# # A1) b: --- Presenting a statistical description of the features ---

# In[904]:


Telco_churn.duplicated().sum()


# In[905]:


Telco_churn = Telco_churn.drop_duplicates(keep='first')


# In[906]:


Telco_churn.shape


# # A2) a: -- (Duplicated data) There are 2 records that exactly match each other --

# In[907]:


Telco_churn['tenure'].min()


# In[908]:


for i in range(Telco_churn.shape[0]):
    if Telco_churn.tenure.loc[i] < 0:
        Telco_churn.tenure.loc[i] = 0
Telco_churn['tenure'].min()


# # A2) b: --- Irrelevant or incorrect values (tenure has negative value) ---

# In[909]:


Telco_churn.isnull().sum()


# In[910]:


#Fill the missing values with the mean of the column
Telco_churn = Telco_churn.fillna(value = Telco_churn['TotalCharges'].mean())
Telco_churn.isnull().sum()


# # A2) c: --- There are 11 Missing values in (TotalCharges) ---

# In[911]:


Telco_churn.drop(["customerID"],axis=1,inplace=True)


# In[912]:


Telco_churn.head()


# #  A3) a: --- Dropping irrelevant data (customer ID) ---

# In[913]:


churn = {'Yes':1, 'No':0}
Telco_churn['Churn'].replace(churn, inplace=True)
Telco_churn


# In[914]:


Telco_churn[['gender','Churn']].groupby(['gender']).mean()*100


# In[915]:


Telco_plot = Telco_churn[['gender','Churn']].groupby(['gender']).mean()*100
plt.figure(figsize=(5,4))
Telco_plot.plot(kind='bar',color='navy')


# # A4) a: -- (Female) percentage which left the company is 26.92%, (Male) percentage which left the company is 26.16%. Since the genders percentages are very close that means that it doesn't have an effect on churn. --

# In[916]:


churn = {1:'Yes', 0:'No'}
Telco_churn.Churn.replace(churn, inplace=True)
senior_citizen = {1:'Yes', 0:'No'}
Telco_churn.SeniorCitizen.replace(senior_citizen, inplace=True)


# In[917]:


plt.figure(figsize=(5,4))
plt.subplot(1,2,1)
sns.countplot(data = Telco_churn , x = 'SeniorCitizen' , hue = 'Churn', palette = "Set1")


# In[918]:


Telco_churn.groupby('SeniorCitizen')['Churn'].value_counts(normalize=True)*100


# # A4) b: -- The percentage of elderly people who left the company is (41.68%) and it indicates that almost half of the senior citizens left so it effects on churn. unlike the non-senior citizens (76.39%) didn't leave and only (23.60%) left. --

# In[919]:


plt.figure(figsize=(6,4))
plt.subplot(1,2,1)
sns.countplot(data = Telco_churn , x = 'Contract' , hue = 'Churn', palette = "Set2")


# In[920]:


Telco_churn.groupby('Contract')['Churn'].value_counts(normalize=True)*100


# # A4) c: -- More than half of customers use a Month-to-month contract option and more customers churn on monthly plans (42.70%) almost half of them, so when a customer has a longer contract the churn gets lower,(11.26%) churned when their contract was One-Year and (2.8%) only churned when their contract was Two-years. --
