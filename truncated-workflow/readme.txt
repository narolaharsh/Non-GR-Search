 ====================coinc-FULL_DATA_FULL-H1L1_ID14_ID0000079====================

         last state: POST_SCRIPT_FAILED
               site: local
        submit file: ./coinc-FULL_DATA_FULL-H1L1_ID14_ID0000079.sub
        output file: coinc-FULL_DATA_FULL-H1L1_ID14_ID0000079.out.015
         error file: coinc-FULL_DATA_FULL-H1L1_ID14_ID0000079.err.015

        -------------------------------Task #1 - Summary--------------------------------

        site        : local
        hostname    : node2123.cluster.ldas.cit
        executable  : /home/soumen.roy/src/npycbc/bin/pycbc_coinc_findtrigs
        arguments   :   --coinc-threshold   0.005   --strict-coinc-time   --ranking-statistic   phasetd_exp_fit_stat_sgveto   --statistic-files   H1L1-PHASE_TIME_AMP_v1.hdf   --timeslide-interval   0.1   --decimation-factor   5000   --loudest-keep-value   8.5   --template-bank   H1L1-BANK2HDF-1126086042-7195.hdf   --trigger-files   H1-HDF_TRIGGER_MERGE_FULL_DATA-1126086042-7195.hdf   L1-HDF_TRIGGER_MERGE_FULL_DATA-1126086042-7195.hdf   --veto-files   H1L1-CUMULATIVE_CAT_12H_VETO_SEGMENTS_CUMULATIVE_CAT_12H-1126086042-7195.xml   --segment-name   CUMULATIVE_CAT_12H   --template-fraction-range   0/20   --output-file   H1L1-COINC_FULL_DATA_FULL_CUMULATIVE_CAT_12H_0-1126086042-7195.hdf  
        exitcode    : 1
        working dir : /local/condor/execute/dir_195641/pegasus.NtNDxGHj4

        ---------Task #1 - coinc-FULL_DATA_FULL-H1L1_ID14 - ID0000079 - stdout----------




        ----Task #1 - coinc-FULL_DATA_FULL-H1L1_ID14 - ID0000079 - Kickstart stderr-----

         Traceback (most recent call last):
  File "/home/soumen.roy/src/npycbc/bin/pycbc_coinc_findtrigs", line 185, in <module>
    rank_method = stat.get_statistic(args.ranking_statistic)(args.statistic_files)
  File "/home/soumen.roy/src/npycbc/lib/python2.7/site-packages/pycbc/events/stat.py", line 483, in __init__
    PhaseTDExpFitStatistic.__init__(self, files)
  File "/home/soumen.roy/src/npycbc/lib/python2.7/site-packages/pycbc/events/stat.py", line 450, in __init__
    ExpFitCombinedSNR.__init__(self, files)
  File "/home/soumen.roy/src/npycbc/lib/python2.7/site-packages/pycbc/events/stat.py", line 420, in __init__
    ExpFitStatistic.__init__(self, files)
  File "/home/soumen.roy/src/npycbc/lib/python2.7/site-packages/pycbc/events/stat.py", line 343, in __init__
    raise RuntimeError("None of the statistic files has the required "
RuntimeError: None of the statistic files has the required attribute called {ifo}-fit_coeffs !