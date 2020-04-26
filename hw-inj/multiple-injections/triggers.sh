pycbc_inspiral --segment-end-pad 64  \
--segment-length 256 \
--segment-start-pad 64 \
--psd-estimation median \
--psd-segment-length 16 \
--psd-segment-stride 8 \
--psd-inverse-length 16 \
--pad-data 8 \
--sample-rate 1024 \
--low-frequency-cutoff 40 \
--strain-high-pass 30 \
--filter-inj-only \
--processing-scheme cpu \
--cluster-method template \
--approximant IMRPhenomD \
--order 8 \
--snr-threshold 5.5 \
--chisq-bins 16 \
--channel-name H1:GDS-CALIB_STRAIN \
--gps-start-time 1126086042 \
--gps-end-time 1126431642 \
--frame-type H1_HOFT_C00 \
--injection-file HL-INJECTIONS_3-1126086042-345600.xml \
--bank-file Feb12.h5 \
--output multiple-injections-output-4-days.hdf \
--verbose

#--trig-start-time 1126086242 \
#--trig-end-time 1126431442 \