#====================================================
#  Question 5
#====================================================
#
# Write a program that accepts a directory name from the user and
# counts the number of files inside it every five minutes.
#
# Write the result into:
#
# DirectoryCountLog.txt
#
# Each entry should contain:
#
# • Directory path
#
# • Number of files
#
# • Date and time
#
#====================================================
import os
import time
from datetime import datetime

def CountFiles(Directory_Name):
    iCount = 0

    for Name in os.listdir(Directory_Name):
        FullPath = os.path.join(Directory_Name, Name)

        if os.path.isfile(FullPath):
            iCount = iCount + 1

    File = open("DirectoryCountLog.txt", "a")

    File.write("Directory Path : " + Directory_Name + "\n")
    File.write("Number of Files : " + str(iCount) + "\n")
    File.write("Date and Time : " + datetime.now().strftime("%d-%m-%Y %I:%M:%S %p") + "\n")
    File.write("-" * 40 + "\n")

    File.close()


def main():
    Directory_Name = input("Enter Directory Name : ")

    while True:
        CountFiles(Directory_Name)
        time.sleep(300)


if __name__ == "__main__":
    main()