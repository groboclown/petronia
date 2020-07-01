#!/bin/bash

set -e

HERE=$( dirname "$0" )

MYPYPATH="${HERE}/../projects/py-common-lib:${MYPYPATH}"

for n in "${HERE}/../projects"/* ; do
  if [ -d "${n}" ] ; then
    pushd "${n}" >/dev/null 2>&1

    # TODO make this platform compatible...
    mypy_packages=""
    lint_packages=""
    for dn in * ; do
      if [ -d "${dn}" ] ; then
        case "${dn}" in
          *_windows)
            # Skip
            x=1
            ;;
          *)
            dx=$( basename "${dn}" )
            mypy_packages="${mypy_packages} --package ${dx}"
            lint_packages="${lint_packages} ${dx}"
            ;;
        esac
      fi
    done

    if [ ! -z "${lint_packages}" ] ; then
      echo "======================================================="
      echo "======================================================="
      echo $( basename "${n}" )
      echo "Type checking..."
      python3 -m mypy --warn-unused-configs --no-incremental ${mypy_packages}

      echo "======================================================="
      echo "Linting..."
      python3 -m pylint ${lint_packages}

      echo "======================================================="
      echo "Running unit tests..."
      python3 -m coverage run --source . -m unittest discover -s . -p "*_test.py"
      python3 -m coverage report -m
    fi
  fi

  popd >/dev/null 2>&1
done

# cd "$HERE/.cache"
# cd "$HERE"
# python3 ./mk_docs.py
