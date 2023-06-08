#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name : ")
print("We will learn how to group by date and plot a line graph for the confidence of the data collected by satellites")
print("Then we will group by date and get the maximum brightness and temperature of the fire")
print("And plot a line graph for showing the correlation between brightness and temperature of fire")


# In[2]:


import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('australia_bushfire.csv')
df


# In[3]:


#Activity 1
#Group by data and plot a line graph for the average confidence of the satellites for collecting data

group_by_date = df.groupby('acq_date')['confidence'].mean().reset_index(name='confidence')
group_by_date



# In[4]:


label = group_by_date['acq_date']
value = group_by_date['confidence']

fig = plt.subplots(figsize=(19,8))

plt.plot(label, value, label = "Average confidence as per date" , linewidth=3.0)
plt.xlabel('Dates')
plt.xticks(rotation='vertical')

plt.ylabel('confidence')

plt.title('Average confidence as per date', fontsize=20)

plt.legend()

plt.show()


# Conclusion - The data captured by the satellite is almost 65 percent confident (accurate)
# 

# In[2]:


#Activity 2
#Show a correlation between the brightness of fire and temperature of fire using line graph

#First - group by date, and find out Max Brightness and create a dataframe out of it
group_by_date_max_brightness=df.groupby('acq_date')['brightness'].max().reset_index()
group_by_date_max_brightness


# In[ ]:


#Second - group by date, and find out Max Temperature and create a dataframe out of it
group_by_date_max_brightness=df.groupby('acq_date')['bright_t31'].max().reset_index()
group_by_date_max_brightness


# In[3]:


#Thrid - get the data and brightness from group by date max brightness and store in respective variable
brightness_label = group_by_date_max_brightness['acq_date']
brightness_value = group_by_date_max_brightness['brightness']

fig = plt.subplots(figsize=(19,8))

#Forth - plot first line graph for max brightness by date
plt.plot(brightness_label, brightness_value, label = "Max Brightness", linewidth=3.0)

#Fifth - get the data and Temperature from group by date max Temperature and store in respective variable
temperature_label = group_by_date_max_temperature['acq_date']
temperature_value = group_by_date_max_temperature['bright_t31']

#Sixth - plot second line graph for max Temperature by date
plt.plot(temperature_label, temperature_value, label = "Max Temperature", linewidth=3.0)


plt.xlabel('Date') 
plt.xticks(rotation='vertical')
           
plt.title('Correlation between the brightness of fire and temperature of fire using line graph', fontsize=20)
           
plt.legend()
           
plt.show()


# Conclusion - 

# In[ ]:




