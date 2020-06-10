WORKFLOW_NAME=o3-3
CONFIG_TAG='v1.16.1.0'
GPSSTART='1249243020'
GPSEND='1249329420'
CHUNKNUMBER='16'
#GITLAB_URL_C00="https://git.ligo.org/ligo-cbc/pycbc-config/raw/${CONFIG_TAG}/O3C00/pipelineHL"
#GITLAB_URL_C01="https://git.ligo.org/ligo-cbc/pycbc-config/raw/${CONFIG_TAG}/O3C01/pipelineHL"

ecp-cookie-init LIGO.ORG https://git.ligo.org/users/auth/shibboleth/callback narola.bharatbhai

pycbc_make_coinc_search_workflow \
  --workflow-name ${WORKFLOW_NAME} --output-dir output \
  --config-files \
  analysis.ini \
  executables.ini \
  injections_minimal.ini \
  plotting.ini \
  gating.ini \
  gps_times.ini \
  data_O3_C01_clean.ini \
  --config-overrides workflow:start-time:${GPSSTART} workflow:end-time:${GPSEND} \
      'results_page:analysis-subtitle:"O3 Analysis '${CHUNKNUMBER}', C01 data"' \
      results_page:output-path:"/home/${USER}/public_html/o3/runs/hl/c01/a${CHUNKNUMBER}_${WORKFLOW_NAME}" \
      workflow:file-retention-level:all_triggers

#GPSEND='1249938637'