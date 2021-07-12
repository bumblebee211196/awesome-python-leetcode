#! /usr/bin/bash

echo "#####  Testing - Sarted  #####"

if [[ -z $1 ]]; then
    pytest --cov=src tests
else
    pytest --cov=src $1
fi

echo "#####  Testing - Ended  #####"