# ==========================================================
# 2. Sum of all Odd Numbers using multiprocessing.Pool
# ==========================================================
#
# Problem:
# Write a Python program using multiprocessing.Pool to
# calculate the sum of all odd numbers from 1 to N
# for every number from the given list.
#
# Input:
# Data = [1000000, 2000000, 3000000, 4000000]
#
# For each N, calculate:
#
# 1 + 3 + 5 + ... + N
#
# Expected Output:
#
# Process ID : 1234
# Input Number : 1000000
# Sum of Odd Numbers : 250000000000
#
# Process ID : 1235
# Input Number : 2000000
# Sum of Odd Numbers : 1000000000000
#
# Process ID : 1236
# Input Number : 3000000
# Sum of Odd Numbers : 2250000000000
#
# Process ID : 1237
# Input Number : 4000000
# Sum of Odd Numbers : 4000000000000
#
# Note:
# Process ID will be different on every computer/run.
#========================================================================================

import time
import multiprocessing
import os

def Sum_Even(No):
    Sum = 0
    for i in range(1,No+1):
        if (i%2!=0):
            Sum = Sum + i

    print(f" Processe Id : {os.getpid()}" f"Input Number : {No}" f" Sum of Even Numbers : {Sum}")
    return Sum
    


def main():

    Data = [1000000, 2000000, 3000000, 4000000]

    Result = []

    Start_Time = time.perf_counter()

    pobj = multiprocessing.Pool()
    Result = pobj.map(Sum_Even,Data)

    pobj.close()
    pobj.join()

    End_Time = time.perf_counter()

    print(Result)

    print(f"Time Required : {End_Time - Start_Time:.4f} Seconds")

if __name__ == "__main__":
    main()
