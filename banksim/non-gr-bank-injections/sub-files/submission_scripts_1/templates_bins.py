#!/usr/bin/env python
# coding: utf-8

# In[25]:


#mchirp window
import numpy as np
import h5py
from pycbc import pnutils
import pickle


# In[31]:


def oneinj(bank, inj, chirp_window):
    #take one injection and creates a bin with templates in mchirp window.
    bank_bin = np.empty((0, 5))
    cm_low = float(inj[4])-chirp_window
    cm_high = float(inj[4])+chirp_window
    
    for row in bank:
        if float(row[4])>= cm_low and float(row[4])<= cm_high:
            bank_bin = np.vstack((bank_bin, row))
    return bank_bin

def create_bins(bank_file, injection_file_address, chirp_window):
    bins = {}
    bank = np.load(bank_file)
    i = 0
    injection_file = np.load(injection_file_address)
    for inj in injection_file:
        bins['injection{0}'.format(i)] = oneinj(bank, inj, chirp_window)
        i = i+1
    return bins


bank_bins = create_bins('Feb12.npy', \
            '/home/narola.bharatbhai/banksim/injection-file/all_params_injection_table.npy', \
           0.5)

pickle.dump(bank_bins, open('bins-5-1.pkl', 'wb'),  pickle.HIGHEST_PROTOCOL)




