#====================================================
#  Question 2
#====================================================
#
# Write a Python program that monitors the size of a specified file
# every 30 seconds.
#
# Write the following details into:
#
# FileSizeLog.txt
#
# • File path
#
# • File size in bytes
#
# • Date and time
#
# Handle the situation where the file does not exist.
#
#====================================================

import os
import sys
import time
import schedule

def Directory(File_Name):

    border = "-"*50

    if os.path.exists(File_Name):

        File_Size = os.path.getsize(File_Name)
        timestamp = time.strftime("%d-%m-%Y %H:%M:%S")

        fobj = open("FileSizeLog.txt","a")

        fobj.write(border + "\n")
        fobj.write("File Path : " + os.path.abspath(File_Name) + "\n")
        fobj.write("File Size : " + str(File_Size) + " Bytes\n")
        fobj.write("Date and Time : " + timestamp + "\n")
        fobj.write(border + "\n")

        fobj.close()

    else:
        print("File does not exist")

def main():

    File_Name = sys.argv[1]

    schedule.every(30).seconds.do(Directory,File_Name)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()