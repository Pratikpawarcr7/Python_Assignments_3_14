# ----------------------------------------------------------
# 10. Threading - Sum and Product of Elements
# Problem:
# Design a Python application that creates
# two threads.
#
# Thread1:
# Compute the sum of all elements from a list.
#
# Thread2:
# Compute the product of all elements from
# the same list.
#
# Return the results to the main thread
# and display them.
#
# Example:
# Input :
# [2, 3, 4, 5]
#
# Sum = 14
# Product = 120
# ----------------------------------------------------------
import threading
import time

def Summation(Numbers):
    Sum = 0
    for iCnt in Numbers:
        Sum = Sum + iCnt
    
    print("Summation : ",Sum)

def Product(Numbers):
    Sum = 1
    for iCnt in Numbers:
        Sum = Sum * iCnt
    
    print("Product : ",Sum)


def main():

    Result = []

    print("How Many Members You Want In Your List : ")
    iValue1 = int(input())

    print("Enter the Number : ")
    for iCnt in range(0,iValue1):
        iValue2 = int(input())
        Result.append(iValue2)
    
    start_time = time.perf_counter()
    print("Your Input List is : ")
    print(Result)

    t1 = threading.Thread(target=Summation,args=(Result,))
    t1.start()
    t1.join()

    t2 = threading.Thread(target=Product,args=(Result,))
    t2.start()
    t2.join()
    end_time = time.perf_counter()

    print(f"Required Time : {end_time - start_time:.5f}")

if __name__ == "__main__":
    main()