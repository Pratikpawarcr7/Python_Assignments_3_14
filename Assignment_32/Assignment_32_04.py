#====================================================
#  Question 4
#====================================================
#
# Write a program that copies all .txt files from one directory to
# another every ten minutes.
#
# The program should:
#
# • Accept source and destination directories
#
# • Validate both directories
#
# • Copy only .txt files
#
# • Maintain a log of copied files
#
# • Avoid terminating if one file cannot be copied
#
#====================================================

import os
import sys
import time
import shutil
import schedule


def Directory(Source, Destination):

    border = "-" * 50

    try:

        # Validate source directory
        if not os.path.isdir(Source):
            print("Source directory does not exist")
            return

        # Validate destination directory
        if not os.path.isdir(Destination):
            print("Destination directory does not exist")
            return

        # Get all files from source directory
        for File_Name in os.listdir(Source):

            if File_Name.endswith(".txt"):

                Source_File = os.path.join(Source, File_Name)
                Destination_File = os.path.join(Destination, File_Name)

                try:

                    shutil.copy2(Source_File, Destination_File)

                    timestamp = time.strftime("%d-%m-%Y %H:%M:%S")

                    # Maintain log
                    fobj = open("CopyLog.txt", "a")

                    fobj.write(border + "\n")
                    fobj.write("File Name : " + File_Name + "\n")
                    fobj.write("Source : " + os.path.abspath(Source_File) + "\n")
                    fobj.write("Destination : " + os.path.abspath(Destination_File) + "\n")
                    fobj.write("Date and Time : " + timestamp + "\n")
                    fobj.write(border + "\n")

                    fobj.close()

                    print(File_Name, "copied successfully")

                except Exception as e:

                    print("Error copying", File_Name, ":", e)

    except Exception as e:

        print("Error :", e)


def main():

    Source = sys.argv[1]
    Destination = sys.argv[2]

    # Run every 10 minutes
    schedule.every(10).minutes.do(Directory, Source, Destination)

    print("Program started...")
    print("Files will be copied every 10 minutes.")

    # Run once immediately
    Directory(Source, Destination)

    while True:

        schedule.run_pending()

        time.sleep(1)


if __name__ == "__main__":
    main()