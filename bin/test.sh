#!/bin/bash

set -e

HERE=$( dirname "$0" )
pushd "${HERE}/../projects/py-common-lib" >/dev/null 2>&1
COMMON_LIB=$(pwd)
popd >/dev/null 2>&1
pushd "${HERE}/../projects/extension-tools" >/dev/null 2>&1
TOOLS_LIB=$(pwd)
popd >/dev/null 2>&1

export PYTHONPATH="${COMMON_LIB}:${TOOLS_LIB}:${PYTHONPATH}"

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
      echo "Running unit tests..."
      python3 -m coverage run --source . -m unittest discover -s . -p "*_test.py"
      python3 -m coverage report -m

      echo "======================================================="
      echo "Linting..."
      python3 -m pylint \
        --load-plugins petronia_extension_tools.pylint_plugins.trailing_commas \
        ${lint_packages} || echo $?
    fi
  fi

  popd >/dev/null 2>&1
done

# cd "$HERE/.cache"
# cd "$HERE"
# python3 ./mk_docs.py
