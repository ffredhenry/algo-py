#!/bin/sh

# Build tester
# runs the list-generator python script several times with hardcoded options
# generates three of varying sizes

# clear out the csv directory
echo "\nCleaning up ~/csvs/..."
rm ~/csvs/*

# smallest
./list-generator.py 100 100000 ~/csvs/hundred.csv

# medium
./list-generator.py 1000 100000 ~/csvs/thousand.csv

# biggest
./list-generator.py 10000 100000 ~/csvs/tenthousand.csv

echo "\nHere are the generated lists:"
ls ~/csvs/*
