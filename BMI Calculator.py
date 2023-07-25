#!/usr/bin/env python
# coding: utf-8

# # BMI Calculator

# In[18]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)


if BMI>0:
    if(BMI<18.5):
        print(name +", You are undeweight.")
    elif(BMI<=24.9):
        print(name +", You are normal weight.")
    elif(BMI<=29.9):
        print(name +", You are overweight.")
    elif(BMI<=34.9):
        print(name +", You are obese.")
    elif(BMI<=39.9):
        print(name +", You are severly obese.")
    else:
        print(name +", You are morbidly obese.")
else:
        print("Enter valid input")


# In[7]:


type(height)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


#BMI = (weight in pounds x 703) / (height in inches x height in inches)


# In[ ]:


under 18.5, Underweight, Minimal
18.5 - 24.9, Normal weight, Minimal
25 - 29.9, Overweight, Increased
30 - 34.9, Obese, High
35 - 39.9, Severly Obese, Very High
40 and over Morbidly Obese, Extremely High


# In[19]:


if BMI>0:
    if(BMI<18.5):
        print(name +",You are undeweight.")
    elif(BMI<=24.9):
        print(name +",You are normal weight.")
    elif(BMI<=29.9):
        print(name +",You are overweight.")
    elif(BMI<=34.9):
        print(name +",You are obese.")
    elif(BMI<=39.9):
        print(name +",You are severly obese.")
    else:
        print(name +",You are morbidly obese.")
else:
    print("Enter valid input")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




