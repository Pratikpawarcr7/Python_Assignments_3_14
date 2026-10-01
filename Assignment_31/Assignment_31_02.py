#====================================================
#  Question 2
#====================================================
#
# Create a function named:
#
# DisplayMessage(message)
#
# Schedule the function using:
#
# schedule.every(5).seconds.do(DisplayMessage, message)
#
# The message should be accepted from the user.
#
#====================================================

import time
import datetime
import schedule

def Display(Name):

    print(Name)

def main():

    
    print("Enter Message : ")
    Name = str(input())

    schedule.every(5).seconds.do(Display,Name)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main() 