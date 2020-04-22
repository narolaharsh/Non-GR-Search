Generate injections using lalapps_inspinj

Remove injections that are outside the bank boundaries

Convert the bankfile from 4X----- to -----X4, so that it is easy to read the templates (saved as a numpy array)

Repeat the same procedure for the injection batch (saved as a numpy array)

We are not using any mchirp window to find nearby templates

Create python scirpts that will be sumitted by a .sub file to HTCondor

For this case we are doing one injection per script, so we for 10,000 injection we have to create total 10,000 .py scripts that would be submitted by .sub file

The output is a numpy array dumped in .pkl file. Numpy array of shape (number of templates x 1)

Another script finds maximum of every array and stores them into a final result file. The final result file is a 10,000 x 1 shaped numpy array. 