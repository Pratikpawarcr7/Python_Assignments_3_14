# ==========================================================
# 3. Count Even Numbers using Pool.map()
# ==========================================================
#
# Problem:
# Write a Python program that counts how many even numbers
# exist between 1 and N using multiprocessing.Pool.map().
#
# Input:
# Data = [1000000, 2000000, 3000000, 4000000]
#
# Expected Output:
#
# Process ID : 1234
# Input Number : 1000000
# Even Number Count : 500000
#
# Process ID : 1235
# Input Number : 2000000
# Even Number Count : 1000000
#
# Process ID : 1236
# Input Number : 3000000
# Even Number Count : 1500000
#
# Process ID : 1237
# Input Number : 4000000
# Even Number Count : 2000000
#
# Note:
# Process ID will be different on every computer/run.
#==============================================================

import time
import multiprocessing
import os

def Sum_Even(No):
    Sum = 0
    for i in range(1,No+1):
        if (i%2==0):
            Sum = Sum + 1

    print(f" Processe Id : {os.getpid()}" f"Input Number : {No}" f" Even Number Count : {Sum}")
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
