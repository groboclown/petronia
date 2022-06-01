#!/bin/bash

# Translates the key symbols from the X11 protocol header files
sources="\
  https://cgit.freedesktop.org/xorg/proto/x11proto/plain/keysymdef.h \
  https://cgit.freedesktop.org/xorg/proto/x11proto/plain/Sunkeysym.h \
  https://cgit.freedesktop.org/xorg/proto/x11proto/plain/XF86keysym.h \
  https://cgit.freedesktop.org/xorg/proto/x11proto/plain/HPkeysym.h \
  https://cgit.freedesktop.org/xorg/proto/x11proto/plain/DECkeysym.h"
# into a Python lookup table.

# (reference)
#   https://cgit.freedesktop.org/xorg/proto/x11proto/plain/specs/keysyms.xml

outfile="$( dirname "$0" )/keysyms_table.py"
tmpdir="/tmp/keysym-$$"

test -f "${outfile}" && rm "${outfile}"
test -d "${tmpdir}" && rm -r "${tmpdir}"
mkdir -p "${tmpdir}"
echo '# GENERATED FILE FROM x11proto symbol files.  DO NOT EDIT.' > "${outfile}"
echo "" >> "${outfile}"
echo "from typing import Sequence, Tuple" >> "${outfile}"
echo "" >> "${outfile}"
echo "KEYSYM_LOOKUP: Sequence[Tuple[int, str]] = (" >> "${outfile}"

for source in ${sources} ; do
  keysym_name="$( basename "${source}" )"
  srcfile="${tmpdir}/${keysym_name}"
  curl -o "${srcfile}" -q -L "${source}"
  line=0
  echo "    # ${source}" >> "${outfile}"

  while IFS="" read -u 10 -r p || [ -n "$p" ]
  do
    line=$(( line + 1 ))
    # strip trailing whitespace
    while [ "${p: -1}" = ' ' ] ; do
      p="${p:0:-1}"
    done
    # reduce duplicate whitespace, replace tabs with spaces, and make lower-case
    p="$( echo "${p}" | tr \\t ' ' | tr -s ' ' | tr '[:upper:]' '[:lower:]' )"
    # Select only the defines.
    if [ "${p:0:8}" = "#define " ] ; then
      keysym=$( echo "${p}" | cut -f 3 -d ' ' )
      if [ ! -z "${keysym}" ] && [ "${keysym}" != '/*' ] ; then

        def_name=$( echo "${p}" | cut -f 2 -d ' ' )
        if [ ! -z "${def_name}" ] ; then
          echo "    (${keysym}, '${def_name}'),  # ${line} definition" >> "${outfile}"
        fi
        part_def=$( echo "${def_name}" | cut -f 2- -d '_' )
        if [ ! -z "${part_def}" ] ; then
          echo "    (${keysym}, '${part_def}'),  # ${line} definition part" >> "${outfile}"
        fi

        # other names are in the comment
        comment_text="$( echo "${p}" | awk 'match($0, /\/\*\s*([^*]+)/, a) {print a[1]}' )"
        while [ "${comment_text: -1}" = ' ' ] ; do
          comment_text="${comment_text:0:-1}"
        done
        if [ "${comment_text:0:10}" = "alias for " ] ; then
          other=$( echo "${comment_text:10}" | cut -f 1 -d ' ' )
          if [ ! -z "${other}" ] ; then
            echo "    (${keysym}, '${other}'),  # ${line} ${comment_text}" >> "${outfile}"
          fi
        elif [ "${comment_text:0:2}" = "U+" ] ; then
          echo "    (${keysym}, '\u${comment_text:2:6}'),  # ${line} unicode" >> "${outfile}"
          other="$( echo "${comment_text:8}" | tr ' -' '__' )"
          if [ ! -z "${other}" ] ; then
            echo "    (${keysym}, '${other}'),  # ${line} unicode name" >> "${outfile}"
          fi
        elif [[ "${comment_test}" = *,* ]] ; then
          # split on ","
          IFS=',' read -ra each_name <<< "${comment_text}"
          for i in "${each_name[@]}" ; do
            # trim whitespace
            while [ "${i:0:1}" = ' ' ] ; do
              i="${i:1}"
            done
            while [ "${i: -1}" = ' ' ] ; do
              i="${i:0:-1}"
            done
            other="$( echo "${i}" | tr ' -' '__' )"
            if [ ! -z "${other}" ] ; then
              echo "    (${keysym}, '${other}'),  # ${line} alias" >> "${outfile}"
            fi
          done
        else
          other="$( echo "${comment_test}" | tr ' -' '__' )"
          if [ ! -z "${other}" ] ; then
            echo "    (${keysym}, '${other}'),  # ${line} ${comment_text}" >> "${outfile}"
          fi
        fi
      fi
    fi

  done 10< "${srcfile}"
  rm "${srcfile}"
done

echo ")" >> "${outfile}"
rm -r "${tmpdir}"
