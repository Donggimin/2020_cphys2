#!/usr/bin/env python
# coding: utf-8

# # 1.구구단 함수

# In[9]:


def 곱하기(a):
    x=[1,2,3,4,5,6,7,8,9]
    return [i*a for i in x]


# In[21]:


곱하기(1),곱하기(2),곱하기(3),곱하기(4),곱하기(5),곱하기(6),곱하기(7),곱하기(8),곱하기(9)


# ## 2.홀수/짝수 판별

# In[29]:


def 판별(a):
    if (a%2==0):
        print ("짝수")
    if (a%2==1):
        print ("홀수")


# In[33]:


판별(200)


# ### 3.평균

# In[30]:


def average(n):
    return sum(n)/len(n)


# In[31]:


average(n=[1,2,3,4,5,6,7,8,9])


# In[ ]:





# In[ ]:




