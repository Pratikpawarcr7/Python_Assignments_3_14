#====================================================
#  Question 3
#====================================================
#
# Write a program that scans a specified directory every minute.
#
# The task should display:
#
# • Directory name
#
# • Number of files
#
# • Number of subdirectories
#
# • Date and time of scanning
#
# Use the os module.
#
# Example output:
#
# Directory Scanned: E:/Data
# Total Files: 15
# Total Subdirectories: 4
# Scan Time: 25-07-2026 04:30:00 PM
#
#====================================================
import os
import time
from datetime import datetime

def ScanDirectory(Directory_Name):
    iFileCount = 0
    iDirectoryCount = 0

    for Name in os.listdir(Directory_Name):
        FullPath = os.path.join(Directory_Name, Name)

        if os.path.isfile(FullPath):
            iFileCount = iFileCount + 1

        elif os.path.isdir(FullPath):
            iDirectoryCount = iDirectoryCount + 1

    print("-" * 40)
    print("Directory Scanned :", Directory_Name)
    print("Total Files :", iFileCount)
    print("Total Subdirectories :", iDirectoryCount)
    print("Scan Time :", datetime.now().strftime("%d-%m-%Y %I:%M:%S %p"))
    print("-" * 40)


def main():
    Directory_Name = input("Enter Directory Name : ")

    while True:
        ScanDirectory(Directory_Name)
        time.sleep(60)


if __name__ == "__main__":
    main()