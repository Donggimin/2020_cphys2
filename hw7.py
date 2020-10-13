#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_sample_image
from sklearn.cluster import KMeans

china = load_sample_image("china.jpg")
image = china/255
plt.imshow(image)


# In[9]:


X = image.reshape(-1,3)
kmeans = KMeans(n_clusters=8).fit(X)


# In[12]:


segmented_img = kmeans.cluster_centers_[kmeans.labels_]
segmented_img = segmented_img.reshape(image.shape)


# In[13]:


plt.imshow(segmented_img)


# In[ ]:




