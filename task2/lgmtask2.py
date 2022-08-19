#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import matplotlib.pyplot as plt


# In[2]:


lotus=cv2.imread("minion2.png",0)


# In[3]:


plt.imshow(lotus)


# In[4]:


grey = cv2.cvtColor(lotus, cv2.COLOR_BGR2RGB)
plt.imshow(grey)


# In[ ]:


invert=255-grey


# In[ ]:


plt.imshow(invert)


# In[ ]:


blur=cv2.GaussianBlur(invert, (111,111),0)


# In[ ]:




