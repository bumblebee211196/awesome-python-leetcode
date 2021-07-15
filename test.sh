#! /usr/bin/bash

echo "#####  Testing - Sarted  #####"

if [[ -z $1 ]]; then
    pytest --cov=src --cov-report=xml --cov-report=term tests
else
    pytest --cov=src --cov-report=xml $1
fi

echo "#####  Testing - Ended  #####"