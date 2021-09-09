#!/bin/sh

set -e

h=$( dirname "$0" )
pd="${h}/../projects"
PYTHONPATH="${pd}/extension-tools:${pd}/py-common-lib" python3 -m petronia_extension_tools.gen_marshal "$@"
