# algo-py: the python algorithm repository
The purpose of this repo is to explore and demonstrate the function of computer
science algorithms with file manipulation (using CSV files of random numbers).

The functional file contains I/O functions for ingressing and egressing data.

### featured algorithms:
* Selection Sort - 0(n^2)
* Insertion Sort - 0(n^2)
* Quick Sort - 0(n*log(n))
* Bubble Sort - 0(n^2)
* Merge Sort - 0(n*log(n))
* Heap Sort - 0(n*log(n))

## additional included funcions

#### buildtest.sh
Generates a series of CSVs in progressively larger sizes for running algorithms against

#### inputoutput.py
Library for functions that are used by the scripts to:
* generate
* ingest
* export
the contents of CSV files for sorting purposes

#### list-generator.py
Uses the inputoutput file as a module for generating CSVs based on command line arguments

#### tripler.py
Proof-of-concept for CSV content manipulation. Also serves as base for additional algorithms

## ideas-list
- Reverse order sorting algorithms (to kick it up a notch)
- time study (how long does each take) + complexity log
- seperate file appends depending on each algorithm used
