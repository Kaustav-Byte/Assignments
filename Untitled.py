#!/usr/bin/env python
# coding: utf-8

# In[11]:


for i in range (2000, 3000,1):
    if i%7== 0 and i/5!=0:
        print (i,',',end="")
    else:
        continue
    


# In[15]:


def my_function(x):
  return x[::-1]

mytxt = my_function(input('Enter your First name= '))
myend =my_function(input('Enter your Second Name= '))
print(mytxt,' ',myend)


# In[17]:


x=(1/6*3.14*12*12*12)
print(x)


# In[ ]:




