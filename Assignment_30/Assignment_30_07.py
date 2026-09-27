
#====================================================
#  Question 7
#====================================================
# 
# Write a Python program that performs a file backup every hour.
# 
# The program should:
# 
# 1. Accept the source file path.
# 2. Accept the destination directory path.
# 3. Copy the source file to the destination directory.
# 4. Add the current date and time to the backup filename.
# 5. Write the backup operation details into:
#    backup_log.txt
# 
# Example backup filename:
# 
# Data_25_07_2026_16_30_00.txt
# 
# Example log entry:
# 
# Backup completed successfully at 25-07-2026 04:30:00 PM
# 
# Use the shutil module for file copying.
# 
#====================================================

import os
import shutil
import datetime
import schedule
import time


def Backup(source, destination):

    try:

        current_time = datetime.datetime.now()

        filename = os.path.basename(source)
        name, extension = os.path.splitext(filename)

        backup_name = name + "_" + current_time.strftime("%d_%m_%Y_%H_%M_%S") + extension

        destination_path = os.path.join(destination, backup_name)

        shutil.copy(source, destination_path)

        log_time = current_time.strftime("%d-%m-%Y %I:%M:%S %p")

        with open("backup_log.txt", "a") as logfile:

            logfile.write("Backup completed successfully at " + log_time + "\n")

        print("Backup completed successfully.")

    except Exception as e:

        print("Backup failed:", e)

def main():

    source = input("Enter source file path: ")
    destination = input("Enter destination directory path: ")

    schedule.every(1).hour.do(Backup, source, destination)

    Backup(source, destination)

    while True:

        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
