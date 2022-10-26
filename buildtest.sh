#!/bin/sh

# Build tester
# runs the list-generator python script several times with hardcoded options
# generates three of varying sizes

#FIXME: add a if statement to check and then create a ~/csvs directory

# clear out the csv directory
echo "\nCleaning up ~/csvs/..."
rm ~/csvs/*

# smallest
./list-generator.py 100 1000 ~/csvs/hundred.csv

# medium
./list-generator.py 1000 10000 ~/csvs/thousand.csv

# biggest
./list-generator.py 10000 100000 ~/csvs/tenthousand.csv

# biggerest
./list-generator.py 100000 1000000 ~/csvs/hundthousand.csv

# biggiggerest
./list-generator.py 1000000 10000000 ~/csvs/millionaire.csv

# biggiggiggerest
./list-generator.py 1000000000 10000000000 ~/csvs/gigalist.csv

echo "\nHere are the generated lists:"
ls ~/csvs/*
