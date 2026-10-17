#!/bin/bash
source '__HERMES_BN_ROOT__/environment.sh'
export DOLT_ROOT_PATH="$HERMES_BN_ROOT/Dolt/local-state"
unset DOLT_REMOTE_USER DOLT_REMOTE_PASSWORD DOLT_CREDS_ID DOLT_CLI_PASSWORD
export NO_COLOR=1
cd "$HERMES_BN_ROOT/Dolt/databases"
