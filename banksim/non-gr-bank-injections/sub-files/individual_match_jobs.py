import numpy as np

gr_injections = np.load('../inj-non-GR-10000-2-attempt20.npy')
batch_size = 1


index = np.arange(0, len(gr_injections), batch_size)
len(index)


string = '''import numpy as np
import csv
from gr_vs_ngr import CalMatch
import copy
import wfutils as lsu
from scipy.interpolate import UnivariateSpline
from math import log, ceil
import lal
from numpy import vectorize, arange, seterr, inf, ones_like
from lal import PI, MSUN_SI, MTSUN_SI, PC_SI, CreateCOMPLEX8FrequencySeries, CreateREAL8Vector, ResizeCOMPLEX16FrequencySeries
import lalsimulation as lalsim
from lalinspiral import CreateSBankWorkspaceCache, InspiralSBankComputeMatch
import pickle
#noise_model = gr_vs_ngr.noise_model

def read_all_params(x):
    w = copy.deepcopy(lsu.ChooseWaveformParams())
    w.mass1 = x[0]
    w.mass2 = x[1]
    w.spin1z = x[2]
    w.spin2x = x[3]
    w.deltaF = 0.01
    lal_prm = lal.CreateDict()
    lalsim.SimInspiralWaveformParamsInsertNonGRDChi1(lal_prm, x[5]) # maximum 2.5
    lalsim.SimInspiralWaveformParamsInsertNonGRDChi2(lal_prm, x[6]) # maximum 5.5 
    lalsim.SimInspiralWaveformParamsInsertNonGRDChi3(lal_prm, x[7]) # maximum 5.5
    lalsim.SimInspiralWaveformParamsInsertNonGRDChi4(lal_prm, x[8]) # maximum 5.5 

    w.nonGRparams = lal_prm
    
    return w

inj_prm = read_all_params(np.load('/home/narola.bharatbhai/banksim/injtest20/inj-non-GR-10000-2-attempt20.npy')[i])
bank = np.load('/home/narola.bharatbhai/banksim/injtest20/attempt10-nonGR.npy')
asd = np.load('/home/narola.bharatbhai/banksim/injtest20/non-GR-bank/pysub/asd14Feb.npy')

match = np.array([])
print 'injection{0}'.format(i)

for t in bank:
    t_prm = read_all_params(t)
    this_match = CalMatch(t_prm, inj_prm, asd)
    match = np.append(match, this_match)

 '''

i = 0
for i in range(0, len(index)):
    print i
    f = open('/home/narola.bharatbhai/banksim/injtest20/non-GR-bank/pysub-2/match.{0}'.format(i), 'w')
    f.write('i = %s \n' %(index[i]))
    f.write(string)
    f.write('\n')
    f.write("pickle.dump(match, open('match{0}.pkl', 'wb') ,pickle.HIGHEST_PROTOCOL)".format(i))
    f.close()



