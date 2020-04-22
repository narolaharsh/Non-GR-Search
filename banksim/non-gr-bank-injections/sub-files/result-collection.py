#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pickle
import glob
import matplotlib.pyplot as plt
import numpy as np


# In[3]:


outfiles = glob.glob('pysub/*pkl')


# In[4]:


len(outfiles)


# In[5]:


match = np.array([])

for i in range(len(outfiles)):
    match = np.append(match, np.max(pickle.load(open('pysub/match%s.pkl' %(i), 'r'))))


# In[6]:


# In[7]:


plt.figure(figsize =  (8, 6))
plt.hist(match, cumulative = 1, log = 1, bins = 50)
plt.title('non-GR Bank vs non-GR Injections')
plt.xlabel('Match')
plt.ylabel('Number of Injections (Cumulative)')
plt.xticks(np.arange(0.90, 1.01, 0.01))
plt.savefig('10000-non-GR-vs-non-GR.png')
plt.show()


# In[8]:


injections = np.load('../inj-non-GR-10000-attempt20.npy')
mass1 = injections[:, 0]
mass2 = injections[:, 1]

plt.figure(figsize =  (8, 6))
plt.scatter(mass1, mass2, c = match, s = 10)
plt.colorbar()
plt.title('non-GR Bank vs non-GR Injections')
plt.xlabel('Mass1')
plt.ylabel('Mass2')
plt.xticks(np.arange(0, 101, 10))
plt.yticks(np.arange(0, 60, 10))
plt.savefig('10000-non-GR-vs-non-GR-m1m2.png')
plt.show()


# In[11]:

