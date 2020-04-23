from __future__ import division
import numpy as np
from numpy import sqrt, sin, cos
import copy

import lal
from lal import PI, MSUN_SI, MTSUN_SI, PC_SI, CreateCOMPLEX8FrequencySeries, CreateREAL8Vector, ResizeCOMPLEX16FrequencySeries
import lalsimulation as lalsim
from lalinspiral import CreateSBankWorkspaceCache, InspiralSBankComputeMatch
from lalinspiral.sbank.psds import noise_models, get_PSD
import wfutils as lsu


def ComputeLALSimFDWaveform(prm, LALParam=None):
    return lalsim.SimInspiralChooseFDWaveform(prm.mass1 * lal.MSUN_SI, prm.mass2 * lal.MSUN_SI,
                0., 0., prm.spin1z, 0., 0., prm.spin2z,
                prm.dist, prm.incl, prm.phiref, 0., 0., 0.,
                prm.deltaF, prm.fmin , prm.fmax, prm.fmin, LALParam, prm.approx)


def CalMatch(tmp_prms, inj_prms, ASD):
    # Create workspace for match calculation
    workspace_cache = CreateSBankWorkspaceCache()
    
    inj_hp, inj_hc = ComputeLALSimFDWaveform(inj_prms, LALParam=inj_prms.nonGRparams)    
    if inj_hc.data.length > len(ASD):
        ASD2 = np.ones(inj_hc.data.length) * np.inf
        ASD2[:len(ASD)] = ASD
        ASD = ASD2
    inj_hc.data.data[:int(inj_prms.fmin/inj_prms.deltaF)] = 0.0
    whiten_inj = lal.CreateCOMPLEX8FrequencySeries(inj_hc.name, -1.0, inj_hc.f0, inj_hc.deltaF, inj_hc.sampleUnits, inj_hc.data.length)
    whiten_inj.data.data[:] = inj_hc.data.data[:]/ASD
    whiten_inj.data.data /= float(np.vdot(whiten_inj.data.data, whiten_inj.data.data).real * 4 * inj_hc.deltaF)**0.5

    tmp_hp, tmp_hc = ComputeLALSimFDWaveform(tmp_prms, LALParam=None)
    tmp_hc.data.data[:int(tmp_prms.fmin/tmp_prms.deltaF)] = 0.0
    whiten_tmp = lal.CreateCOMPLEX8FrequencySeries(tmp_hc.name, -1.0, tmp_hc.f0, tmp_hc.deltaF, tmp_hc.sampleUnits, tmp_hc.data.length)
    whiten_tmp.data.data[:] = tmp_hc.data.data[:]/ASD
    whiten_tmp.data.data /= float(np.vdot(whiten_tmp.data.data, whiten_tmp.data.data).real * 4 * tmp_hc.deltaF)**0.5

    return InspiralSBankComputeMatch(whiten_inj, whiten_tmp, workspace_cache)



    



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

PSD = get_PSD(tmp_params.deltaF, inj_params.fmin, inj_params.fmax, noise_models["aLIGOZeroDetHighPower"])
ASD = np.sqrt(PSD)

print CalMatch(tmp_params, inj_params, ASD)



