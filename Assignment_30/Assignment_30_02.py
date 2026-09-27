# =========================================================================
# Q2) Display Current Date and Time Every One Minute
# =========================================================================
#
# Problem Statement:
# Write a Python program that displays the current date
# and time after every one minute.
#
# Use the datetime module.
#
# Expected Output:
#
# Current Date and Time: 25-07-2026 04:30:00 PM
#==========================================================================

import datetime
import schedule
import time

def Display():

    print("Current Date and Time : ",datetime.datetime.now())


def main():

    schedule.every(1).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()













