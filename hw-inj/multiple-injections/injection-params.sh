lalapps_inspinj --gps-start-time 1126086042 \
    --gps-end-time 1126431642 \
    --f-lower 30.0 \
    --min-mtotal 10.0 --max-mtotal 100.0 \
    --min-spin1 0.0 --max-spin1 0.998 \
    --min-spin2 0. --max-spin2 0.998 \
    --min-mratio 1.0 --max-mratio 10.0 \
    --i-distr uniform --fixed-inc 0 \
    --m-distr totalMassRatio \
    --min-distance 1000. \
    --max-distance 1000. \
    --l-distr random \
    --waveform IMRPhenomDpseudoFourPN \
    --aligned \
    --enable-spin \
    --d-distr uniform \
    --time-step 600 \
    --time-interval 25 \
    --seed 3

#1126086042 2015-09-12T09:40:25
#1126431642 2015-09-16T09:40:25
#--time-interval 0. \
