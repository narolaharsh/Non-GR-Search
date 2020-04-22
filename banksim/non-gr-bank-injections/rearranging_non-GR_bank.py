#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import matplotlib.pyplot as plt
import h5py
from pycbc import pnutils
import csv


# In[10]:


f = h5py.File('attempt10-nonGR.h5', 'r')

mass1 = f['mass1'][:]
mass2 = f['mass2'][:]
spin1z = f['spin1z'][:]
spin2z = f['spin2z'][:]
deltaChi1 = f['deltaChi1'][:]
deltaChi2 = f['deltaChi2'][:]
deltaChi3 = f['deltaChi3'][:]
deltaChi4 = f['deltaChi4'][:]


# In[11]:


len(mass1)


# In[4]:


'''pspin = csv.reader(open('pspin-bank.txt'), delimiter = '\t')

mass1 = np.array([])
mass2 = np.array([])
spin1z = np.array([])
spin2z = np.array([])

for row in pspin:
    mass1 = np.append(mass1, float(row[0]))
    mass2 = np.append(mass2, float(row[1]))
    spin1z = np.append(spin1z, float(row[2]))
    spin2z = np.append(spin2z, float(row[3])) '''


# In[12]:


mchirp = np.array([])

i = 0
for i in range(len(mass1)):
        mc, _ = pnutils.mass1_mass2_to_mchirp_eta(float(mass1[i]), float(mass2[i]))
        mchirp = np.append(mchirp, mc)



bank_array = np.array([mass1, mass2, spin1z, spin2z, mchirp, deltaChi1, deltaChi2,                      deltaChi3, deltaChi4]).T          

#index = np.argsort(mchirp)
#bank_array = bank_array[index]

#np.save('Feb12.npy', bank_array)


# In[13]:


np.save('attempt10-nonGR.npy', bank_array)


# In[14]:


bank_array.shape


