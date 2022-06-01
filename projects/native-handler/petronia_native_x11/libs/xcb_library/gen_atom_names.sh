#!/bin/bash

# The atomlist.m4 file comes from the xcb-util-wm library,
#   located under ewmh/atomlist.m4

if [ "$1" = "-h" ] || [ "$1" = "--help" ] ; then
  echo "Generates atomlist.py list from atomlist.m4"
  exit 0
fi

src_dir=$( pwd )
if [ -d "$1" ] ; then
  src_dir="$1"
elif [ ! -z "$1" ]; then
  echo "Could not find directory '$1'"
  exit 1
fi
if [ ! -f "${src_dir}/atomlist.m4" ] ; then
  echo "${src_dir} must include the file atomlist.m4"
  echo "This file comes from xcb-util-wm, ewmh/atomlist.m4"
  exit 1
fi

test -f "${src_dir}/atomlist.py" && rm "${src_dir}/atomlist.py"
echo '# GENERATED FILE FROM atomlist.m4.  DO NOT EDIT.' > "${src_dir}/atomlist.py"
echo "" >> "${src_dir}/atomlist.py"
echo "from typing import Sequence" >> "${src_dir}/atomlist.py"
echo "" >> "${src_dir}/atomlist.py"
echo 'ATOM_NAMES: Sequence[bytes] = (' >> "${src_dir}/atomlist.py"
while IFS="" read -u 10 -r p || [ -n "$p" ]
do
  while [ "${p:0}" = ' ' ] ; do
    p="${p:1-}"
  done
  while [ "${p: -1}" = ',' ] || [ "${p: -1}" = ')' ] || [ "${p: -1}" = ' ' ] ; do
    p="${p:0:-1}"
  done
  if [ "${p}" != 'DO(' ] && [ "${p}" != ')' ] && [ ! -z "${p}" ] ; then
    # printf '%s\n' "$p"
    echo "    b'${p}'," >> "${src_dir}/atomlist.py"
  fi
done 10< "${src_dir}/atomlist.m4"
echo ")" >> "${src_dir}/atomlist.py"
