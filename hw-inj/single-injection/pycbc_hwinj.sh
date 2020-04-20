pycbc_generate_hwinj --high-frequency-cutoff 1024.0 \
--geocentric-end-time 1124381661 \
--gps-start-time H1:1124380361 \
--gps-end-time H1:1124382409 \
--frame-type H1:H1_HOFT_C00 \
--channel-name H1:GDS-CALIB_STRAIN \
--approximant IMRPhenomD \
--order pseudoFourPN \
--mass1 25.0 \
--mass2 25.0 \
--inclination 0.0 \
--polarization 0.0 \
--ra 0.0 \
--dec 0.0 \
--taper TAPER_START \
--network-snr 28 \
--waveform-low-frequency-cutoff 30.0 \
--low-frequency-cutoff 30.0 \
--sample-rate 1024 \
--pad-data 8 \
--strain-high-pass 30.0 \
--psd-estimation median \
--psd-segment-length 16 \
--psd-segment-stride 8 \
--instruments H1


#1124380361 2015-08-23T15:52:24
#1124382409 2015-08-23T16:26:32
#1124381661 2015-08-23T16:14:04
