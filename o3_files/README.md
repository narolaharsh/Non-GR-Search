# O3 C00 data 2-ifo Pipeline Configuration Files #

This directory contains the necessary PyCBC workflow configuration files to
run the ``pycbc_make_coinc_search_workflow`` generator on ER14 or O3 C00 data.

## Analysis Configuration ##

The files

 * analysis.ini
 * plotting.ini
 * executables.ini
 * injections_minimal.ini

are the primary workflow configuration files.  In addition files named eg data.ini, gating.ini, gps_times.ini are used to give specific information about the data to be run on and data quality.

Instructions to create a workflow by directly pulling these files at runtime (after having sourced PyCBC released version 1.15.4).  NOTE that 'albert.einstein' should be replaced by your @ligo.org login name!
```
WORKFLOW_NAME=o3
CONFIG_TAG='v1.15.6.0'
GPSSTART='YOUR_START_TIME'
GPSEND='YOUR_END_TIME'
CHUNKNUMBER='YOUR_ANALYSIS_NUMBER'
GITLAB_URL="https://git.ligo.org/ligo-cbc/pycbc-config/raw/${CONFIG_TAG}/O3C00/pipelineHL"

ecp-cookie-init LIGO.ORG https://git.ligo.org/users/auth/shibboleth/callback albert.einstein

pycbc_make_coinc_search_workflow \
  --workflow-name ${WORKFLOW_NAME} --output-dir output \
  --config-files \
  ${GITLAB_URL}/analysis.ini \
  ${GITLAB_URL}/executables.ini \
  ${GITLAB_URL}/injections_minimal.ini \
  ${GITLAB_URL}/plotting.ini \
  ${GITLAB_URL}/data_O3_C00.ini \
  ${GITLAB_URL}/gating.ini \
  ${GITLAB_URL}/gps_times.ini \
  --config-overrides workflow:start-time:${GPSSTART} workflow:end-time:${GPSEND} \
      'results_page:analysis-subtitle:"O3 Analysis '${CHUNKNUMBER}', C00 data"' \
      results_page:output-path:"/home/${USER}/public_html/o3/runs/hl/c00/a${CHUNKNUMBER}_initial" \
      workflow:file-retention-level:all_triggers
```

To then submit the workflow do:
```
cd output
pycbc_submit_dax --accounting-group ligo.prod.o3.cbc.bbh.pycbcoffline --dax o3.dax --no-grid
```

For further details including run diagnosis and debugging see [this link](https://pycbc.org/pycbc/latest/html/workflow/pycbc_make_coinc_search_workflow.html#monitor-and-debug-the-workflow-detailed-pegasus-documentation).