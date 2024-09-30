#!/bin/bash

# Activate virtual environment for Git Bash (Windows)
# activate the virtual environment
source ./venv/Scripts/activate

# Debugging: Check if the virtual environment is active
# which python

# navigate to the src directory where the test file is located
cd src

# run the test suite
python -m pytest test_visualization.py

# collect exit code from pytest
# exit code is 0 if all tests pass
PYTEST_EXIT_CODE=$?

# return exit code 0 if all tests pass or 1 otherwise
if [ $PYTEST_EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1
fi