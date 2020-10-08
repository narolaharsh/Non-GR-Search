from __future__ import division
import numpy as np
from numpy import sqrt, sin, cos
import copy

import lal
from lal import PI, MSUN_SI, MTSUN_SI, PC_SI, CreateCOMPLEX8FrequencySeries, CreateREAL8Vector, ResizeCOMPLEX16FrequencySeries
import lalsimulation as lalsim
from lalinspiral import CreateSBankWorkspaceCache, InspiralSBankComputeMatch
#from lalinspiral.sbank.psds import noise_models, get_PSD
import wfutils as lsu



from scipy.interpolate import UnivariateSpline
from math import log, ceil

from numpy import vectorize, arange, seterr, inf, ones_like
seterr(over="ignore") # the PSD overflows frequently, but that's OK


# Supply the path of the PSD file
data = np.loadtxt("/home/narola.bharatbhai/banksim/Jan22-bank/H1L1-AVERAGE_PSD-1128643217-86400.txt")

f_orig, psddata = data[:,0], data[:,1]
f_max_orig = 2048.0 #max(f_orig)
interpolator = UnivariateSpline(f_orig, np.log(psddata), s=0)
noise_model = lambda g: np.where(g < f_max_orig, np.exp(interpolator(g)), np.inf)

psd_cache = {}  # keyed by df, flow, f_max
def get_PSD(df, flow, f_max, noise_model):
    """
    Return the frequency vector and sampled PSD using the noise_model,
    which are vectorized wrappings of the noise models in lalsimulation.
    flow sets the first non-zero frequency.
    """
    if (df, flow, f_max) in psd_cache:
        return psd_cache[df, flow, f_max]
    f = arange(f_max / df + 1) * df
    LIGO_PSD = inf * ones_like(f)
    ind_low = int(flow / df)
    LIGO_PSD[ind_low:] = noise_model(f[ind_low:])
    return psd_cache.setdefault((df, flow, f_max), LIGO_PSD)







def ComputeLALSimFDWaveform(prm, LALParam=None):
    return lalsim.SimInspiralChooseFDWaveform(prm.mass1 * lal.MSUN_SI, prm.mass2 * lal.MSUN_SI,
                0., 0., prm.spin1z, 0., 0., prm.spin2z,
                prm.dist, prm.incl, prm.phiref, 0., 0., 0.,
                prm.deltaF, prm.fmin , prm.fmax, prm.fmin, LALParam, prm.approx)


def CalMatch(tmp_prms, inj_prms, ASD):
    # Create workspace for match calculation
    workspace_cache = CreateSBankWorkspaceCache()
    
    #inj_hp, inj_hc = ComputeLALSimFDWaveform(inj_prms, LALParam=inj_prms.nonGRparams) 
    inj_hp, inj_hc = ComputeLALSimFDWaveform(inj_prms, LALParam=None) 
    if inj_hc.data.length > len(ASD):
        ASD2 = np.ones(inj_hc.data.length) * np.inf
        ASD2[:len(ASD)] = ASD
        ASD = ASD2
    inj_hc.data.data[:int(inj_prms.fmin/inj_prms.deltaF)] = 0.0
    whiten_inj = lal.CreateCOMPLEX8FrequencySeries(inj_hc.name, -1.0, inj_hc.f0, inj_hc.deltaF, inj_hc.sampleUnits, inj_hc.data.length)
    whiten_inj.data.data[:] = inj_hc.data.data[:]/ASD
    whiten_inj.data.data /= float(np.vdot(whiten_inj.data.data, whiten_inj.data.data).real * 4 * inj_hc.deltaF)**0.5
##################################made some changes############################
    tmp_hp, tmp_hc = ComputeLALSimFDWaveform(tmp_prms, LALParam=None)
    #tmp_hp, tmp_hc = ComputeLALSimFDWaveform(tmp_prms, LALParam=tmp_prms.nonGRparams)
    tmp_hc.data.data[:int(tmp_prms.fmin/tmp_prms.deltaF)] = 0.0
    whiten_tmp = lal.CreateCOMPLEX8FrequencySeries(tmp_hc.name, -1.0, tmp_hc.f0, tmp_hc.deltaF, tmp_hc.sampleUnits, tmp_hc.data.length)
    whiten_tmp.data.data[:] = tmp_hc.data.data[:]/ASD
    whiten_tmp.data.data /= float(np.vdot(whiten_tmp.data.data, whiten_tmp.data.data).real * 4 * tmp_hc.deltaF)**0.5

    return InspiralSBankComputeMatch(whiten_inj, whiten_tmp, workspace_cache)



    

'''

inj_params = copy.deepcopy(lsu.ChooseWaveformParams())
inj_params.mass1 = 7.0
inj_params.mass2 = 5.0
inj_params.spin1z = 0.0
lal_prm = lal.CreateDict()
lalsim.SimInspiralWaveformParamsInsertNonGRDChi1(lal_prm, 0.0) # maximum 2.5
lalsim.SimInspiralWaveformParamsInsertNonGRDChi2(lal_prm, 0.0) # maximum 5.5 
lalsim.SimInspiralWaveformParamsInsertNonGRDChi3(lal_prm, 0.1) # maximum 5.5
lalsim.SimInspiralWaveformParamsInsertNonGRDChi4(lal_prm, 0.0) # maximum 5.5 

inj_params.nonGRparams = lal_prm

tmp_params = copy.deepcopy(lsu.ChooseWaveformParams())
tmp_params.mass1 = 7.0
tmp_params.mass2 = 5.0
tmp_params.spin1z = 0.0

# Use 'noise_model' to extract required sampled PSD from a PSD file.
PSD = get_PSD(tmp_params.deltaF, inj_params.fmin, inj_params.fmax, noise_models["aLIGOZeroDetHighPower"])
ASD = np.sqrt(PSD)

print CalMatch(tmp_params, inj_params, ASD)
'''


