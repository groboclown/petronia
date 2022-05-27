#!/bin/bash

if [ "$1" = "--help" ] || [ "$1" = "-h" ] ; then
  echo "Usage: $0 [--xephyr (WIDTHxHEIGHT) (:DISPLAY)]"
  echo "Normal execution will just run Petronia connecting to the default X11 server (using"
  echo "\$DISPLAY)."
  echo ""
  echo "If you run with the '--xephyr' argument, then the script will launch the command"
  echo "'xephyr', which is an x server-in-x.  Xephyr will launch with the given width/height"
  echo "on the given display number."
  exit 0
fi

if [ "$1" = "--xephyr" ] ; then
  shift
  screen_size="$1"
  shift
  display="$1"
  shift
  Xephyr -br -ac -noreset -screen "${screen_size}" "${display}" &
  echo "Started Xephyr on process $!"
  export DISPLAY="${display}"
fi

scriptdir=$( dirname "$0" )
here=$( cd "${scriptdir}" ; pwd )
PROJECTS="${here}/projects"
SETUP="${here}/example-setup/linux-x11"
LANGUAGE=en_US

export PYTHONPATH="${PROJECTS}/foreman:${PROJECTS}/py-common-lib:${PROJECTS}/py-extension-lib:${PROJECTS}/extension-loader:${PROJECTS}/extension-runner:${PROJECTS}/native-handler:${PROJECTS}/core-extensions:${PROJECTS}/portal:${PROJECTS}/ui-extensions"

python -m petronia_foreman -c "${SETUP}/petronia.ini" --config-dir "${SETUP}/system/config" --config-dir "${SETUP}/user" --data-dir "${SETUP}/system/data" --data-dir "${PROJECTS}/l10n/compiled" "$@"

# python3 -c "import time ; from petronia_native_x11.libs import setup ; setup.setup_x11(use_argb_visual=True, replace_existing_wm=True) ; time.sleep(500)"
