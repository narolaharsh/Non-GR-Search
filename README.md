# Non-GR-Search
## Template based search for deviation from General Relativity from gravitational wave signals

This branch has the modules to place templates over an 8 dimensional parameter space. 2 masses, 2 spins, and four non-GR parameters

The banksim module tries to mimick the pycbc_banksim module. 

There are two main scripts:  single_injection_match and make_ngr_banksim

single_injection_match: Reads an injection with injection id i from the injection.xml file, calculates the match with the entire template bank and stores it in .pkl file. 

make_ngr_banksim: Facilitates the use of HTCondor. This script creates jobs N number of jobs which are to be submitted to job scheduler. Where N is the total number of injections in the file. 

We are using LIGO CalTech cluster to run this jobs. 
