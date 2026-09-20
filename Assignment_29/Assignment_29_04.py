#===================================================================================
# Q4) Compare Two Files (Command Line)
#
# Problem Statement:
# Write a program which accepts two file names through
# command line arguments and compares the contents of both files.
#
# If both files contain the same contents, display Success.
# Otherwise display Failure.
#
# Input (Command Line):
# Demo.txt Hello.txt
#
# Expected Output:
# Success OR Failure
#=======================================================================================

import sys

if len(sys.argv) < 3:
    print("Please provide two file names")
    exit()

File1 = sys.argv[1]
File2 = sys.argv[2]

fobj1 = open(File1, "r")
fobj2 = open(File2, "r")

Data1 = fobj1.read()
Data2 = fobj2.read()

if Data1 == Data2:
    print("Success")
else:
    print("Failure")

fobj1.close()
fobj2.close()

