# ----------------------------------------------------------
# 4. Threading - Small, Capital and Digits
# Problem:
# Design a Python application that creates three
# threads named Small, Capital, and Digits.
#
# All threads should accept a string as input.
#
# Small Thread:
# Count and display the number of lowercase characters.
#
# Capital Thread:
# Count and display the number of uppercase characters.
#
# Digits Thread:
# Count and display the number of numeric digits.
#
# Each thread should also display:
# 1. Thread ID
# 2. Thread Name
#
# Example:
# Input :
# "Marvellous123"
#
# Small Characters  = 9
# Capital Characters = 1
# Digits = 3
#
# Each thread should display its Thread ID
# and Thread Name.
# ----------------------------------------------------------

import time
import threading


def Check_Small(No1):
    
    Count = 0
    for iCnt in No1:
         if ord(iCnt) >= 97 and ord(iCnt) <= 122:
            Count = Count + 1
   
    print("Count of Small Letter is",Count)

def Check_Capital(No1):
    
    Count = 0
    for iCnt in No1:
         if ord(iCnt) >= 65 and ord(iCnt) <= 90:
            Count = Count + 1
   
    print("Count of Capital Letter is",Count)

def Check_Digit(No1):
    
    Count = 0
    for iCnt in No1:
        if iCnt in "0123456789": 
            Count = Count + 1
   
    print("Count of Digit is",Count)
            

def main():
   print("Enter the String : ")
   iValue1 = input()

   start_time = time.perf_counter()

   Small_Thread = threading.Thread(target = Check_Small,args = (iValue1,))
   Small_Thread.start()
   Small_Thread.join()

   Capital_Thread = threading.Thread(target = Check_Capital,args = (iValue1,))
   Capital_Thread.start()
   Capital_Thread.join()

   Digits_Thread = threading.Thread(target = Check_Digit,args = (iValue1,))
   Digits_Thread.start()
   Digits_Thread.join()

   end_time = time.perf_counter()

   print(f"Require Time : {end_time - start_time:.4f}")

   
if __name__ == "__main__":
    main()
