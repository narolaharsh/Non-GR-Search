
WORKFLOW_NAME=inspiral-job
GITHUB_URL="https://raw.githubusercontent.com/ligo-cbc/pycbc-config/97d0bbcddf17cf91b70b54834598e9d4e150fc8e/O2/pipeline"
OUTPUT_PATH=${HOME}/public_html/LSC/o1/${WORKFLOW_NAME}

pycbc_make_coinc_search_workflow \
    --workflow-name ${WORKFLOW_NAME} \
    --output-dir output \
    --config-files \
        analysis.ini \
        data.ini \
        plotting.ini \
        injections.ini \
        gps_times_O2_analysis_18.ini \
        executables.ini \
    --config-overrides \
        "results_page:output-path:${OUTPUT_PATH}" \
        "workflow:end-time:1126093237" \
    --config-delete \
        'workflow-coincidence' \
        

#1126093237 : 12-09-15 11:40:20
#two hours of data