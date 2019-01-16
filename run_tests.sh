#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color



# Run the testsuite
echo "Running tests"
python -m unittest discover -s statsd_wrap/tests/

# Run the flake8
printf "\n\n===== Running flake tests =====\n"
python -m flake8 --ignore E501
if [ $? -eq 0 ]
then
    printf "${GREEN}SUCCESSS!${NC}\n"
else
    printf "${RED}FAILED!${NC}\n"
fi

# Run mypy
echo -e "\n\n===== Output from mypy ====="
MYPYPATH=$PYTHONPATH mypy .
if [ $? -eq 0 ]
then
    printf "${GREEN}SUCCESSS!${NC}\n"
else
    printf "${RED}FAILED!${NC}\n"
fi