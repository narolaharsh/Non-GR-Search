WORKFLOW_NAME=o3-run-trial
CONFIG_TAG='v1.16.1'
GPSSTART=1126086042
GPSEND=1126431642
CHUNKNUMBER='1'
GITLAB_URL="https://git.ligo.org/ligo-cbc/pycbc-config/raw/${CONFIG_TAG}/O3C00/pipelineHL"
OUTPUT_PATH=${HOME}/public_html/LSC/o1/${WORKFLOW_NAME}


ecp-cookie-init LIGO.ORG https://git.ligo.org/users/auth/shibboleth/callback narola.bharatbhai

pycbc_make_coinc_search_workflow \
  --workflow-name ${WORKFLOW_NAME} --output-dir output-trial \
  --config-files \
  analysis.ini \
  executables.ini \
  injections_minimal.ini \
  plotting.ini \
  data_O3_C00.ini \
  gating.ini \
  gps_times.ini \
  --config-overrides workflow:start-time:${GPSSTART} workflow:end-time:${GPSEND} \
  "results_page:output-path:${OUTPUT_PATH}" \
      workflow:file-retention-level:all_triggers
