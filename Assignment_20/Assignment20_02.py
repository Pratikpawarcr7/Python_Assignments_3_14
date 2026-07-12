# ----------------------------------------------------------
# 2. Threading - EvenFactor and OddFactor
# Problem:
# Design a Python application that creates two threads named EvenFactor and OddFactor.
# 
# Both threads should accept one integer number as a parameter.
# 
# EvenFactor Thread:
# 1. Identify all even factors of the given number.
# 2. Calculate and display the sum of even factors.
#
# OddFactor Thread:
# 1. Identify all odd factors of the given number.
# 2. Calculate and display the sum of odd factors.
#
# After both threads complete execution,the main thread should display:
#
# Output: Exit from main
# 
# Example: Input : 12
# 
# Even Factors:2 4 6 12
# Sum = 24
#
# Odd Factors: 1 3
# Sum = 4
#
# Output:
# Exit from main
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

     print("Enter the Number : ")
     iValue = int(input())


     start_time = time.perf_counter()

     for iCnt in range(1,iValue+1):
         if iValue % iCnt == 0:
             if iCnt % 2 ==0:
                Result.append(iCnt)
             else:
                ResultX.append(iCnt)

     print("Even Factors Are :",Result)

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
    

