import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as et
import csv
import h5py
from pycbc import pnutils
import pickle 


inj = csv.reader(open('injections100000.txt'), delimiter = '\t')

gr_params = np.empty((0, 4))

for row in inj:
    if float(row[0]) >= 5 and float(row[0]) <=100 and     float(row[1]) >= 5 and float(row[1]) <= 100:
        row = np.array([float(x) for x in row])
        gr_params = np.append(gr_params, [row], axis = 0) 
        
print len(gr_params), type(gr_params),gr_params.shape 



mchirp = np.array([])

for i in range(len(gr_params)):
    mc, _ = pnutils.mass1_mass2_to_mchirp_eta(gr_params[i, 0], float(gr_params[i, 1]))
    mchirp = np.append(mchirp, mc)
    


gr_params = np.column_stack((gr_params, mchirp))


#np.save('inj-GR-10000-attempt20.npy', gr_params[0:10000])


# In[7]:


delta_phi_1 = np.random.uniform(-0.894, 2.701, len(gr_params))
delta_phi_2 = np.random.uniform(-0.66, 1.806, len(gr_params))
delta_phi_3 = np.random.uniform(-1.127, 0.419, len(gr_params))
delta_phi_4 = np.random.uniform(-3.552, 8.35, len(gr_params))

delta_phi = np.array([delta_phi_1, delta_phi_2, delta_phi_3, delta_phi_4])
delta_phi = delta_phi.T

all_params = np.concatenate((gr_params, delta_phi), axis = 1)
np.save('inj-non-GR-10000-2-attempt20.npy', all_params[10000:20000])
#all_params is a (1000, 8) numpy array: mass1, mass2, spin1, spin2, mchirp, deltaPhi --arranged


# In[13]:





# In[ ]:




