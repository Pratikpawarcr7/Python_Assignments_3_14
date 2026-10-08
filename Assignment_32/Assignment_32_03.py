#====================================================
#  Question 3
#====================================================
#
# Write a program that reads and displays the contents of a specified
# text file every minute.
#
# Handle the following conditions:
#
# • File does not exist
#
# • File is empty
#
# • Permission is denied
#
# • File cannot be opened
#
#====================================================
import os
import sys
import time
import schedule

def DisplayFile(File_Name):

    if not os.path.exists(File_Name):
        print("File does not exist")
        return

    if os.path.getsize(File_Name) == 0:
        print("File is empty")
        return

    try:
        fobj = open(File_Name, "r")

        Data = fobj.read()

        print("File Contents :")
        print(Data)

        fobj.close()

    except PermissionError:
        print("Permission denied")

    except OSError:
        print("File cannot be opened")


def main():

    File_Name = sys.argv[1]

    schedule.every(1).minutes.do(DisplayFile, File_Name)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()