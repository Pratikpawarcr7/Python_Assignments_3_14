#=========================================================================
# Q3) Copy File Contents into a New File (Command Line)
#
# Problem Statement:
# Write a program which accepts an existing file name through
# command line arguments, creates a new file named Demo.txt,
# and copies all contents from the given file into Demo.txt.
#
# Input (Command Line):
# ABC.txt
#
# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt.
#===========================================================================

import sys

if len(sys.argv) < 2:
    print("Please provide a file name")
    exit()

SourceFile = sys.argv[1]

fobj1 = open(SourceFile, "r")

fobj2 = open("Demo.txt", "w")

Data = fobj1.read()

fobj2.write(Data)

fobj1.close()
fobj2.close()

print("Contents copied successfully into Demo.txt")