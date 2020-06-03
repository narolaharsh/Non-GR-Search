WORKFLOW_NAME=o3_workflow_inj
CONFIG_TAG='v1.16.1'
GPSSTART=1126086042
GPSEND=1126431642
CHUNKNUMBER=01
#GITLAB_URL="https://git.ligo.org/ligo-cbc/pycbc-config/raw/${CONFIG_TAG}/O3C00/pipelineHL"

ecp-cookie-init LIGO.ORG https://git.ligo.org/users/auth/shibboleth/callback narola.bharatbhai

pycbc_make_coinc_search_workflow \
  --workflow-name ${WORKFLOW_NAME} --output-dir output \
  --config-files \
  analysis.ini \
  executables.ini \
  injections_minimal.ini \
  plotting.ini \
  data_O3_C00.ini \
  gating.ini \
  gps_times.ini \
  --config-overrides workflow:start-time:${GPSSTART} workflow:end-time:${GPSEND} \
      'results_page:analysis-subtitle:"O3 Analysis '${CHUNKNUMBER}', C00 data"' \
      results_page:output-path:"/home/${USER}/public_html/o3/runs/hl/c00/a${CHUNKNUMBER}_reproduce" \
      workflow:file-retention-level:all_triggers

