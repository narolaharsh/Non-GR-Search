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
--gps-start-time 1124380361 \
--gps-end-time 1124382409 \
--trig-start-time 1124381659 \
--trig-end-time 1124381663 \
--frame-type H1_HOFT_C00 \
--injection-file hwinjcbc_1124381655.xml.gz \
--bank-file hwinjcbc_1124381655.xml.gz \
--output one-inj-output.hdf \
--verbose

#pycbc_inspiral --segment-end-pad 64  --segment-length 256 --segment-start-pad 64 --psd-estimation median --psd-segment-length 16 --psd-segment-stride 8 --psd-inverse-length 16 --pad-data 8 --sample-rate 4096 --low-frequency-cutoff 40 --strain-high-pass 30 --filter-inj-only --processing-scheme cpu --cluster-method template --approximant SEOBNRv2 --order 8 --snr-threshold 5.5 --chisq-bins 16 --channel-name ${CHANNEL_NAME} --gps-start-time ${GPS_START_TIME} --gps-end-time ${GPS_END_TIME} --trig-start-time $(($GEOCENT_END_TIME - 2)) --trig-end-time $(($GEOCENT_END_TIME + 2)) --frame-type ${FRAME_TYPE} --injection-file ${TMPLTBANK_FILE}  --bank-file ${TMPLTBANK_FILE} --output ${INSPIRAL_FILE} --verbose