#!/bin/python3

# ---------- inputoutput.py
# Contains functions used for creating and intaking data

# ---------- Imported Modules
import csv
import random

# ---------- CSV Ingress Function
# Takes a single argument (the path to the .csv file) and returns an array with its contents

def ingressCSV(location):
    numlist = []
    with open(location) as f:
        readhead = csv.reader(f)
        for row in readhead:
            for col in range(len(row)):
                numlist.append(int(row[col]))
    return numlist

# ---------- CSV Generate Function
# Takes three input arguments:
#   How many numbers (span)
#   Range of numbers (limit)
#   Path of file to write to (location)
# 
# No returned function value, but random numbers
# are generated in a row and written to a CSV

def generateCSV(span,limit,location):
    row = []
    f = open(location,'w')
    writehead = csv.writer(f)

    for i in range(1,span):
        row.append(random.randint(1,limit))

    writehead.writerow(row)
    f.close()

# Sanity check
#print("Calling generateCSV function:\n\n")
#generateCSV(10,100,'./test.csv')

#print("Calling ingressCSV function:\n")
#numdata = ingressCSV("./test.csv")
#print("Result:\n{}".format(numdata))
