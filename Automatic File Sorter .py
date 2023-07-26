#!/usr/bin/env python
# coding: utf-8

# # Automatic File Sorter in File Explorer

# In[6]:


import os, shutil


# In[20]:


path = r"C:/Users/ethanm/OneDrive - Boulder Centre for Orthopedics/Desktop/Python File Sorter/"


# In[23]:


file_name = os.listdir(path)


# In[30]:


folder_names = ['csv files', 'sql files', 'image files']

for loop in range(0,3):    
    if not os.path.exists(path + folder_names[loop]):
        #print(path + folder_names[loop])
        os.makedirs(path + folder_names[loop])


for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".sql" in file and not os.path.exists(path + "sql files/" + file):
        shutil.move(path + file, path + "sql files/" + file)


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




