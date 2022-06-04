#!/bin/bash

# The atomlist.m4 file comes from the xcb-util-wm library,
#   located under ewmh/atomlist.m4

if [ "$1" = "-h" ] || [ "$1" = "--help" ] ; then
  echo "Generates atomlist.py list from *atomlist.m4"
  exit 0
fi

src_dir=$( pwd )
if [ -d "$1" ] ; then
  src_dir="$1"
elif [ ! -z "$1" ]; then
  echo "Could not find directory '$1'"
  exit 1
fi

outfile="${src_dir}/atomlist.py"
test -f "${outfile}" && rm "${outfile}"

echo '# GENERATED FILE FROM atomlist.m4.  DO NOT EDIT.' > "${outfile}"
echo "" >> "${outfile}"
echo "from typing import Sequence" >> "${outfile}"
echo "" >> "${outfile}"
echo 'ATOM_NAMES: Sequence[bytes] = (' >> "${outfile}"

partial="${src_dir}/partial"
test -f "${partial}" && rm "${partial}"
for fn in "${src_dir}/"*atomlist.m4 ; do

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
      echo "    b'${p}'," >> "${partial}"
    fi
  done 10< "${fn}"

done

cat "${partial}" | sort | uniq >> "${outfile}"
rm "${partial}"
echo ")" >> "${outfile}"
