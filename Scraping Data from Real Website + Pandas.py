#!/usr/bin/env python
# coding: utf-8

# # Scraping Data from Real Website + Pandas

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[4]:


url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')


# In[5]:


print(soup)


# In[6]:


soup.find('table')


# In[9]:


soup.find_all('table')[1]


# In[11]:


soup.find('table', class_ = 'wikitable sortable')


# In[10]:


table = soup.find_all('table')[1]


# In[12]:


print(table)


# In[27]:


world_titles = table.find_all('th')


# In[28]:


world_titles


# In[30]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[31]:


import pandas as pd


# In[32]:


df = pd.DataFrame(columns = world_table_titles)

df


# In[36]:


column_data = table.find_all('tr')


# In[44]:


for row in column_data[1:]:
    row_data = (row.find_all('td'))
    individual_row_data = [data.text.strip() for data in row_data]

    length = len(df)
    df.loc[length] = individual_row_data


# In[45]:


df


# In[51]:


df.to_csv(r'C:\Users\ethanm\OneDrive - Boulder Centre for Orthopedics\Desktop\Python File Sorter\csv files\companies.csv', index = False)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




