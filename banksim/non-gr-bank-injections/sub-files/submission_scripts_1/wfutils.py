from __future__ import division

import sys
import copy
import types
from math import cos, sin, sqrt
import numpy as np


import lal
from lal import PI, MSUN_SI, MTSUN_SI, PC_SI, CreateCOMPLEX8FrequencySeries, CreateREAL8Vector, ResizeCOMPLEX16FrequencySeries
import lalsimulation as lalsim
import lalinspiral
from lalinspiral.sbank.psds import noise_models, get_PSD
from lalinspiral import CreateSBankWorkspaceCache, InspiralSBankComputeMatch
#import pycbc



#
# Class to hold arguments of ChooseWaveform functions
#
class ChooseWaveformParams:
    """
    Class containing all the arguments needed for SimInspiralChooseTD/FDWaveform
    plus parameters theta, phi, psi, radec to go from h+, hx to h(t)
    if radec==True: (theta,phi) = (DEC,RA) and strain will be computed using
            XLALSimDetectorStrainREAL8TimeSeries
    if radec==False: then strain will be computed using a simple routine 
            that assumes (theta,phi) are spherical coord. 
            in a frame centered at the detector
    """
    def __init__(self, phiref=0., deltaT=1./4096., mass1=10.*lal.MSUN_SI,
            mass2=10.*lal.MSUN_SI, spin1x=0., spin1y=0., spin1z=0.,
            spin2x=0., spin2y=0., spin2z=0., fmin=15., fref=15., dist=1.e6*lal.PC_SI,
            incl=0., lambda1=0., lambda2=0., waveFlags=None, nonGRparams=None,
            ampO=-1, phaseO=-1, approx=lalsim.IMRPhenomD, 
            theta=0., phi=0., psi=0., tref=0., radec=False, detector="H1",
            deltaF=0.1, fmax=2048., # for use w/ FD approximants
            taper=lalsim.SIM_INSPIRAL_TAPER_NONE # for use w/TD approximants
            ):
        self.phiref = phiref
        self.deltaT = deltaT
        self.mass1 = mass1
        self.mass2 = mass2
        self.spin1x = spin1x
        self.spin1y = spin1y
        self.spin1z = spin1z
        self.spin2x = spin2x
        self.spin2y = spin2y
        self.spin2z = spin2z
        self.fmin = fmin
        self.fref = fref
        self.dist = dist
        self.incl = incl
        self.lambda1 = lambda1
        self.lambda2 = lambda2
        self.waveFlags = waveFlags
        self.nonGRparams = nonGRparams
        self.ampO = ampO
        self.phaseO = phaseO
        self.approx = approx
        self.theta = theta     # DEC.  DEC =0 on the equator; the south pole has DEC = - pi/2
        self.phi = phi         # RA.   
        self.psi = psi
        # FIXME: make into property
        self.longAscNodes = self.psi
        # FIXME: Allow to be a value at some point
        self.eccentricity = 0.0
        self.meanPerAno = 0.0
        self.tref = tref
        self.radec = radec
        self.detector = "H1"
        self.deltaF=deltaF
        self.fmax=fmax
        self.fISCO = 0.0
        self.taper = taper

    _LAL_DICT_PARAMS = {"Lambda1": "lambda1", "Lambda2": "lambda2", "ampO": "ampO", "phaseO": "phaseO"}
    _LAL_DICT_PTYPE = {"Lambda1": lal.DictInsertREAL8Value, "Lambda2": lal.DictInsertREAL8Value, "ampO": lal.DictInsertINT4Value, "phaseO": lal.DictInsertINT4Value}
    def to_lal_dict(self):
        extra_params = lal.CreateDict()
        for k, p in ChooseWaveformParams._LAL_DICT_PARAMS.iteritems():
            typfunc = ChooseWaveformParams._LAL_DICT_PTYPE[k]
            typfunc(extra_params, k, getattr(self, p))
        # Properly add tidal parammeters
        lalsim.SimInspiralWaveformParamsInsertTidalLambda1(extra_params, self.lambda1)
        lalsim.SimInspiralWaveformParamsInsertTidalLambda2(extra_params, self.lambda2)
        return extra_params
    
    
    

