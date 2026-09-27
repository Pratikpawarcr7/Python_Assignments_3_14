# ==========================================================
# Q5) Write Current Date and Time into a File
# ==========================================================
# Problem Statement:
# Schedule a task that executes every five minutes.
#
# The task should write the current date and time into
# a file named:
#
# Marvellous.txt
#
# New entries should be appended without removing
# previous entries.
#
# Example file contents:
#
# Task executed at: 25-07-2026 04:30:00 PM
# Task executed at: 25-07-2026 04:35:00 PM
# Task executed at: 25-07-2026 04:40:00 PM
#==============================================================
import datetime
import schedule
import time

def Display():

    timestamp = time.ctime() # new

    LogFileName = "Marvellous%s.log"%(timestamp)  
    LogFileName = LogFileName.replace(" ","_") 
    LogFileName = LogFileName.replace(":","_")
    fobj = open(LogFileName,"w")

    
    print("Log File gets created with name : ",LogFileName)


def main():

    schedule.every(1).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()













