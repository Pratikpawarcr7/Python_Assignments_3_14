# ----------------------------------------------------------
# 3. Threading - EvenList and OddList
# Problem:
# Design a Python application that creates two
# threads named EvenList and OddList.
#
# Both threads should accept a list of integers
# as input.
#
# EvenList Thread:
# 1. Extract all even elements from the list.
# 2. Calculate and display the sum of even elements.
#
# OddList Thread:
# 1. Extract all odd elements from the list.
# 2. Calculate and display the sum of odd elements.
#
# Both threads should run concurrently using
# the threading module.
#
# Example:
# Input :
# [10, 11, 12, 13, 14, 15]
#
# Even Elements:
# 10 12 14
# Sum = 36
#
# Odd Elements:
# 11 13 15
# Sum = 39
# ----------------------------------------------------------

import time
import threading

def Even_Factors(no):

    Sum = 0
    
    for iCnt in no:
        Sum = Sum + iCnt
    print("Sum :",Sum)
    

def Odd_Factors(no):
    Sum = 0
    
    for iCnt in no:
        Sum = Sum + iCnt
    print("Sum :",Sum)
    
def main():
     
     Result = []
     ResultX = []
     ResultXX = []

     print("Enter the Number of Elemets that you Want in Your List : ")
     iValue = int(input())

     print("Enter the Elements : ")
     for iCnt in range(0,iValue):
         iNum = int(input())
         ResultXX.append(iNum)
     print("Your Input List is : ",ResultXX)

     
     start_time = time.perf_counter()

     for iCnt in ResultXX:
         if iCnt % 2 == 0:
                Result.append(iCnt)
         else:
                ResultX.append(iCnt)

     print("Even Even List Are :",Result)

     t1 = threading.Thread(target=Even_Factors,args = (Result,))
     t1.start()
     t1.join()

     print("Odd Factors Are :",ResultX)

     t2 = threading.Thread(target=Odd_Factors,args = (ResultX,))
     t2.start()
     t2.join()

     end_time = time.perf_counter()
     
     print(f"Time Required is :{end_time - start_time:.4f}")

     print("Exit from main ")

if __name__ == "__main__":
    main()
    


