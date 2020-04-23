lalapps_inspinj --gps-start-time 1126368017 \
    --gps-end-time 1130371217 \
    --f-lower 30.0 \
    --min-mtotal 10.0 --max-mtotal 100.0 \
    --min-spin1 0.0 --max-spin1 0.998 \
    --min-spin2 0. --max-spin2 0.998 \
    --min-mratio 1.0 --max-mratio 10.0 \
    --i-distr fixed --fixed-inc 0 \
    --m-distr totalMassRatio \
    --min-distance 1000. \
    --max-distance 1000. \
    --l-distr random \
    --waveform IMRPhenomDpseudoFourPN \
    --aligned \
    --enable-spin \
    --d-distr uniform \
    --time-step 604800 \
    --seed 3

#1126368017 150915 16 00 00
#1130371217 151101 00 00 00
#--time-interval 0. \
