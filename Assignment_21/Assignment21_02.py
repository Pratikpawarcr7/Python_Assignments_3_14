# ----------------------------------------------------------
# 2. Threading - Maximum and Minimum Element
# Problem:
# Design a Python application that creates two
# threads.
#
# Thread1:
# Calculate and display the maximum element
# from a list.
#
# Thread2:
# Calculate and display the minimum element
# from the same list.
#
# The list should be accepted from the user.
#
# Example:
# Input :
# [10, 50, 20, 5, 80]
#
# Maximum Element = 80
# Minimum Element = 5
# ----------------------------------------------------------

import threading
import time
import os

def Maximum(Data):

    Max = Data[0]
    for iCnt in range(len(Data)):
        if(Data[iCnt] > Max):
            Max = Data[iCnt]
    
    print("Id od Maximum Number is",threading.get_ident())
    print("Maximum Elements",Max)

def Minimum(Data):

    Min = Data[0]
    for iCnt in range(len(Data)):
        if(Data[iCnt] < Min):
            Min = Data[iCnt]
    
    print("Id od Minimum Number is",threading.get_ident())
    print("Minimum Elements",Min)


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

    t1 = threading.Thread(target=Maximum,args=(Result,))
    t1.start()
    t1.join()

    t2 = threading.Thread(target=Minimum,args=(Result,))
    t2.start()
    t2.join()
    end_time = time.perf_counter()

    print(f"Required Time : {end_time - start_time:.5f}")

if __name__ == "__main__":
    main()