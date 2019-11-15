#!/bin/sh

set -e

HERE=$( dirname "$0" )

mkdir -p "$HERE/../i18n"
pybabel extract -o "$HERE/../i18n/messages.pot" --sort-by-file --copyright-holder="Petronia" -c "I18N" "$HERE/../src"
