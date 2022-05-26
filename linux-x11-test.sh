#!/bin/bash

scriptdir=$( dirname "$0" )
here=$( cd "${scriptdir}" ; pwd )
PROJECTS="${here}/projects"
SETUP="${here}/example-setup/linux-x11"
LANGUAGE=en_US

export PYTHONPATH="${PROJECTS}/foreman:${PROJECTS}/py-common-lib:${PROJECTS}/py-extension-lib:${PROJECTS}/extension-loader:${PROJECTS}/extension-runner:${PROJECTS}/native-handler:${PROJECTS}/core-extensions:${PROJECTS}/portal"

python -m petronia_foreman -c "${SETUP}/petronia.ini" --config-dir "${SETUP}/system/config" --config-dir "${SETUP}/user" --data-dir "${SETUP}/system/data" --data-dir "${PROJECTS}/l10n/compiled" "$@"

# python3 -c "import time ; from petronia_native_x11.libs import wm_connect ; wm_connect.connect_as_window_manager(on_server_init=[], use_argb_visual=True, replace_existing_wm=True) ; time.sleep(500)"
