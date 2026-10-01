#====================================================
#  Question 1
#====================================================
#
# Write a program that accepts:
#
# • A message from the user
#
# • A time interval in seconds
#
# Schedule the program to display the message repeatedly after the
# specified interval.
#
# Example input:
#
# Enter message: Jay Ganesh
# Enter interval in seconds: 5
#
# Expected output:
#
# Jay Ganesh
# every five seconds.
#
# Validate that the interval is greater than zero.
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

    print("Enter interval in seconds : ")
    iValue1 = int(input())

    schedule.every(5).seconds.do(Display,Name)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main() 