#!/bin/bash

set -e

HERE=$( dirname "$0" )

test -d $HERE/.cache || mkdir $HERE/.cache
rsync -a $HERE/../src/ $HERE/.cache

case "$( uname )" in
    Linux)
        rm -r $HERE/.cache/petronia/defimpl/platform/windows
        ;;
    Cygwin)
        # If you're using Cygwin to run a Windows version of
        # Python, or even to run Petronia, then you're doing
        # things wrong.
        rm -r $HERE/.cache/petronia/defimpl/platform/windows
        ;;
    *)
               exit 1
        ;;
esac

cd "$HERE/.cache"
echo "======================================================="
echo "Type checking..."
python3 -m mypy --warn-unused-configs --no-incremental \
    --package petronia
echo "======================================================="
echo "Linting..."
python3 -m pylint -j 3 -E petronia
echo "======================================================="
echo "Running unit tests..."
python3 -m coverage run --source . -m unittest discover -s . -p "*_test.py"
python3 -m coverage report -m
