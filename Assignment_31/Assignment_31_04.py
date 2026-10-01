#====================================================
#  Question 4
#====================================================
#
# Write a program that creates a new log file after every ten minutes.
#
# The filename should contain the current date and time.
#
# Example:
#
# MarvellousLog_25_07_2026_16_30_00.txt
#
# The file should contain:
#
# Log file created successfully.
# Creation Time: 25-07-2026 04:30:00 PM
#
#====================================================

import time
from datetime import datetime

def CreateLogFile():
    CurrentTime = datetime.now()

    FileName = "MarvellousLog_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    File = open(FileName, "w")

    File.write("Log file created successfully.\n")
    File.write("Creation Time: " + CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))

    File.close()

    print("Log File Created :", FileName)


def main():
    while True:
        CreateLogFile()
        time.sleep(600)


if __name__ == "__main__":
    main()