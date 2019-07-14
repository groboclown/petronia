#!/bin/bash

set -e

HERE=$( dirname "$0" )

cd "$HERE/../src"
echo "======================================================="
echo "Type checking..."
python3 -m mypy --warn-unused-configs --no-incremental --package petronia3
echo "======================================================="
echo "Running unit tests..."
python3 -m unittest discover -s . -p "*_test.py"
