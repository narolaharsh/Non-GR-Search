# Non-GR-Search
## Template based search for deviation from General Relativity from gravitational wave signals

This branch has the modules to place templates over an 8 dimensional parameter space. 2 masses, 2 spins, and four non-GR parameters

The banksim module tries to mimick the pycbc_banksim module but pycbc_banksim doesn't allow the non-GR parameters.   

There are two main scripts:  single_injection_match and make_ngr_banksim

single_injection_match: Reads an injection with injection id i from the injection.xml file, calculates the match with the entire template bank and stores it in .pkl file. 

make_ngr_banksim: Facilitates the use of HTCondor. This script creates jobs N number of jobs which are to be submitted to job scheduler. Where N is the total number of injections in the file. 

Input files required: An injection file in (.xml) format with sim_inspiral table, a bank file in (.hdf) format, and a suitable asd file

How to create a non-GR injection file?
Generate a regular injection file with lalapps_inspinj. 
Use ligolw package to piggy-back the deltaPhi parameters in alpha1, alpha2, alpha3, and alpha4 columns of the sim_inspriral table. 
We have made sure that these columns are otherwise unused in a PyCBC search so it will not interfere with rest of the stages such as matched filtering, coincidence test etc

We are using LIGO CalTech cluster to run this jobs. 

A similar module is being used to test non-GR bank. 
