#!/bin/bash

if [ "$1" = "--help" ] || [ "$1" = "-h" ] ; then
  echo "Usage: $0 [--xephyr (WIDTHxHEIGHT) (:DISPLAY)] [--client]"
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
use_client=0
if [ "$1" = "--client" ] ; then
  use_client=1
  shift
elif [ "$1" = "--simplest" ] ; then
  use_client=2
  shift
fi


scriptdir=$( dirname "$0" )
here=$( cd "${scriptdir}" ; pwd )
PROJECTS="${here}/projects"
SETUP="${here}/example-setup/linux-wayland"
LANGUAGE=en_US

export PYTHONPATH="${PROJECTS}/foreman:${PROJECTS}/py-common-lib:${PROJECTS}/py-extension-lib:${PROJECTS}/extension-loader:${PROJECTS}/extension-runner:${PROJECTS}/native-handler:${PROJECTS}/core-extensions:${PROJECTS}/portal:${PROJECTS}/ui-extensions"

if [ "${use_client}" = 0 ] ; then
  python -m petronia_foreman \
      -c "${SETUP}/petronia.ini" \
      --config-dir "${SETUP}/system/config" \
      --config-dir "${SETUP}/user" \
      --data-dir "${SETUP}/system/data" \
      --data-dir "${PROJECTS}/l10n/compiled" \
      "$@"
elif [ "${use_client}" = 1 ] ; then
  python3 projects/native-handler/petronia_native_wayland/libs/xcb_library/new_win_cli.py
elif [ "${use_client}" = 2 ] ; then
  python3 projects/native-handler/petronia_native_wayland/libs/simplest_wm_cli.py
fi

# python3 -c "import time ; from petronia_native_x11.libs import setup ; setup.setup_x11(use_argb_visual=True, replace_existing_wm=True) ; time.sleep(500)"
