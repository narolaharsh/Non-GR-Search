import copy
import numpy as np
import wfutils as lsu
import lal
import lalsimulation as lalsim


def read_gr_params(x):
    # reads GR params of the signal
    #x must be in an array format with mass1, mass2, spin2z, spin2z order
    w = copy.deepcopy(lsu.ChooseWaveformParams())
    w.mass1 = x[0]
    w.mass2 = x[1]
    w.spin1z = x[2]
    w.spin2z = x[3]
    w.deltaF = 0.001
    return w
    
def read_all_params(x):
    # reads all params of the signal
    #x must be in an array format with mass1, mass2, spin2z, spin2z, delta Chi 1, 2, 3, 4 order
    w = copy.deepcopy(lsu.ChooseWaveformParams())
    w.mass1 = x[0]
    w.mass2 = x[1]
    w.spin1z = x[2]
    w.spin2z = x[3]
    w.deltaF = 0.001
    lal_prm = lal.CreateDict()
    lalsim.SimInspiralWaveformParamsInsertNonGRDChi1(lal_prm, x[4]) 
    lalsim.SimInspiralWaveformParamsInsertNonGRDChi2(lal_prm, x[5])  
    lalsim.SimInspiralWaveformParamsInsertNonGRDChi3(lal_prm, x[6]) 
    lalsim.SimInspiralWaveformParamsInsertNonGRDChi4(lal_prm, x[7])

    w.nonGRparams = lal_prm
    
    return w