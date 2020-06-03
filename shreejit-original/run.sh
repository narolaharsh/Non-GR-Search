WORKFLOW_NAME=o3
CONFIG_TAG='v1.15.3.0'
GPSSTART='1249243020'
GPSEND='1249938637'
CHUNKNUMBER='16'
GITLAB_URL_C00="https://git.ligo.org/ligo-cbc/pycbc-config/raw/${CONFIG_TAG}/O3C00/pipelineHL"
GITLAB_URL_C01="https://git.ligo.org/ligo-cbc/pycbc-config/raw/${CONFIG_TAG}/O3C01/pipelineHL"

ecp-cookie-init LIGO.ORG https://git.ligo.org/users/auth/shibboleth/callback shreejit.jadhav

pycbc_make_coinc_search_workflow \
  --workflow-name ${WORKFLOW_NAME} --output-dir output \
  --config-files \
  ${GITLAB_URL_C00}/analysis.ini \
  ${GITLAB_URL_C00}/executables.ini \
  ${GITLAB_URL_C00}/injections_minimal.ini \
  ${GITLAB_URL_C00}/plotting.ini \
  ${GITLAB_URL_C00}/gating.ini \
  ${GITLAB_URL_C00}/gps_times.ini \
  ${GITLAB_URL_C01}/data_O3_C01_clean.ini \
  --config-overrides workflow:start-time:${GPSSTART} workflow:end-time:${GPSEND} \
      'results_page:analysis-subtitle:"O3 Analysis '${CHUNKNUMBER}', C01 data"' \
      results_page:output-path:"/home/${USER}/public_html/o3/runs/hl/c01/a${CHUNKNUMBER}_${DESCRIPTION}" \
      workflow:file-retention-level:all_triggers
