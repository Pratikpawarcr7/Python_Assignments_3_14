#====================================================
#  Question 5
#====================================================
#
# Write a program that deletes all empty files from a specified
# directory every hour.
#
# The program should:
#
# • Scan the directory recursively
#
# • Detect files whose size is zero bytes
#
# • Delete the empty files
#
# • Store deleted file paths in a log file
#
# • Handle permission errors
#
# Test the program only on a sample directory.
#
#====================================================

import os
import sys
import time
import schedule


def DeleteEmptyFiles(Directory):

    border = "-" * 50

    # Validate directory
    if not os.path.isdir(Directory):
        print("Directory does not exist")
        return

    # Scan directory recursively
    for Root, Dirs, Files in os.walk(Directory):

        for File_Name in Files:

            File_Path = os.path.join(Root, File_Name)

            try:

                # Check file size
                if os.path.getsize(File_Path) == 0:

                    # Delete empty file
                    os.remove(File_Path)

                    timestamp = time.strftime("%d-%m-%Y %H:%M:%S")

                    # Store deleted file path in log
                    fobj = open("DeleteLog.txt", "a")

                    fobj.write(border + "\n")
                    fobj.write("Deleted File : " + File_Path + "\n")
                    fobj.write("Date and Time : " + timestamp + "\n")
                    fobj.write(border + "\n")

                    fobj.close()

                    print("Deleted:", File_Path)

            except PermissionError:

                print("Permission denied:", File_Path)

            except Exception as e:

                print("Error:", File_Path, e)


def main():

    Directory = sys.argv[1]

    # Run every 1 hour
    schedule.every(1).hours.do(DeleteEmptyFiles, Directory)

    print("Program started...")
    print("Empty files will be deleted every hour.")

    # Run once immediately
    DeleteEmptyFiles(Directory)

    while True:

        schedule.run_pending()

        time.sleep(1)


if __name__ == "__main__":
    main()