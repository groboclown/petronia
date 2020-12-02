#!/bin/sh

h=$( dirname "$0" )
pd="${h}/../projects"
PYTHONPATH="${pd}/extension-tools:${pd}/py-common-lib" exec python3 -m petronia_extension_tools.gen_marshal "$@"
