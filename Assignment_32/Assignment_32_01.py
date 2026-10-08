#====================================================
#  Question 1
#====================================================
#
# Write a program that creates a new text file every minute.
#
# The filename should contain the current timestamp.
#
# Example:
#
# File_25_07_2026_16_30_00.txt
#
# Write the following information into the file:
#
# • Filename
#
# • Creation date
#
# • Creation time
#
#====================================================

import os
import sys
import time
import schedule

def Directory(Dirctory_Name):

    border = "-"*50
    timestamp = time.ctime()

    LogFileName = "File%s.txt"%(timestamp)
    LogFileName = LogFileName.replace(" ","_")  
    LogFileName = LogFileName.replace(":","_")



    fobj = open(LogFileName,"w")
    fobj.write(border + "\n")
    fobj.write("Output : \n")
    fobj.write(border + "\n")
    fobj.write(LogFileName)
    fobj.write("\n" + border + "\n")
    fobj.write("Filename : " + LogFileName + "\n")
    fobj.write(border + "\n")
    fobj.write("Creation Date : " + time.strftime("%d-%m-%Y") + "\n")
    fobj.write(border + "\n")
    fobj.write("Creation Time : " + time.strftime("%H:%M:%S") + "\n")
    fobj.write(border + "\n")
    fobj.write("Creation Date : " + time.strftime("%d-%m-%Y") + "\n")
    



def main():

    DirectoryName = sys.argv[1]

    schedule.every(1).minutes.do(Directory,DirectoryName)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()

