#!/bin/python3

# ---------- inputoutput.py
# Contains functions used for the creating, importing and exporting
# series of randomly-generated integers to a CSV file. This is used
# as a module in the algo-py scripts to simply and expedite coding.

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

# ---------- CSV Egress Function
# Takes two input arguments:
#   List to write to file (the "row")
#   Path of file to write to (location)
#
# No returned value(s), only closes a file

def egressCSV(row,location):
    
    # create a new file with -sorted
    # location = location[:-4]+"-sorted"+location[-4:]

    # open file to write
    f = open(location,'w')
    writehead = csv.writer(f)

    # write the row to file and close
    writehead.writerow(row)
    f.close()

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

# ---------- Debugging Below Here

# Sanity check
#print("Calling generateCSV function:\n\n")
#generateCSV(10,100,'./test.csv')

#print("Calling ingressCSV function:\n")
#numdata = ingressCSV("./test.csv")
#print("Result:\n{}".format(numdata))

#lateral = [8,6,7,5,3,0,9]
#egressCSV(lateral,"./guggis.csv")
