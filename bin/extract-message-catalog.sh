#!/bin/sh

set -e

HERE=$( dirname "$0" )

for n in "${HERE}"/../projects/* ; do
  if [ -d "${n}" ] ; then
    project_name=$( basename "${n}" )
    mkdir -p "$HERE/../l10n/${project_name}"
    pybabel extract \
      -o "${HERE}/../l10n/${project_name}/messages.pot" \
      --sort-by-file \
      --copyright-holder="Petronia" \
      -c "I18N" \
      "${n}"
  fi
done
