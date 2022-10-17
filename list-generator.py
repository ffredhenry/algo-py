#!/bin/python3

# ---------- Testing script
# Uses command line arguments to call functions


# ---------- Imported modules

import inputoutput as io
import csv
import sys

# ---------- Main

# command line args passed to variables
rspan = int(sys.argv[1])
rlim = int(sys.argv[2])
ofile =sys.argv[3]

print("Your params:\n")
print("\tCSV size: {}".format(rspan))
print("\tNumber range: 1 - {}".format(rlim))
print("\tOutput file: {}".format(ofile))
print("\nGenerating a CSV!")
io.generateCSV(rspan,rlim,ofile)
