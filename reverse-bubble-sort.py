#!/bin/python3

# ---------- REVERSE Bubble Sort Algorithm
# Python implementation of bubble sort algorithm
# uses the csv, and inputoutput modules to import
# CSVs and sort the numbers in a list before writing
# to a CSV file with an appended -sorted title.

# ---------- Imported modules
import inputoutput as io
import csv
import sys


# ---------- Main
target = sys.argv[1]

# ingress of data
numdata = io.ingressCSV(target)

# bubble sort operation
for i in range(len(numdata)):
        for j in range(0,len(numdata)-i-1):
            if numdata[j] < numdata[j+1]: #FIXME: flipped comparative op
                numdata[j], numdata[j+1] = numdata[j+1], numdata[j]

# finishing up, appending "-bubblesorted" to CSV
target = target[:-4]+"-REV-bubblesorted"+target[-4:]
print("Sorting complete! Writing to file.")
io.egressCSV(numdata,target)
