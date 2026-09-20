#================================================================================================
# Q1) Check File Exists in Current Directory
#
# Problem Statement:
# Write a program which accepts a file name from the user
# and checks whether that file exists in the current directory or not.
#
# Input:
# Demo.txt
#
# Expected Output:
# Display whether Demo.txt exists or not.
#================================================================================================

import os

FileName = input("Enter file name : ")


if os.path.exists(FileName):
    print(FileName, "exists in current directory")
else:
    print(FileName, "does not exist in current directory")
