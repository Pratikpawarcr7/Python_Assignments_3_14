# ==========================================================
# Q1) Print "Jay Ganesh..." Every 2 Seconds
# ==========================================================
# Problem Statement:
#
# Write a Python program that prints:
#
# Jay Ganesh...
#
# every two seconds.
#
# Use:
# schedule.every(2).seconds.do(...)
#
# Expected Output:
#
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...
# ===========================================================

import datetime
import schedule
import time

def Display():

    print("Jay Ganesh...",datetime.datetime.now())


def main():

    schedule.every(1).seconds.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()













