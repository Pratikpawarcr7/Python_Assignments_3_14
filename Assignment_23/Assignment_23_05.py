# ==========================================================
# 5. Factorial of Multiple Numbers using multiprocessing.Pool
# ==========================================================
#
# Problem:
# Write a Python program that calculates factorials of
# multiple numbers simultaneously using multiprocessing.Pool.
#
# Input:
# Data = [10, 15, 20, 25]
#
# For every N, calculate:
#
# N!
#
# Expected Output:
#
# Process ID : 1240
# Input Number : 10
# Factorial : 3628800
#
# Process ID : 1241
# Input Number : 15
# Factorial : 1307674368000
#
# Process ID : 1242
# Input Number : 20
# Factorial : 2432902008176640000
#
# Process ID : 1243
# Input Number : 25
# Factorial : 15511210043330985984000000
#
# Note:
# Process ID will be different on every computer/run.
# ==========================================================

import time
import multiprocessing
import os

def Sum_Even(No):
    Sum = 1
    for i in range(1,No+1):
        Sum = Sum * i

    print(f" Processe Id : {os.getpid()}" f"Input Number : {No}" f" Factorial : {Sum}")
    
    return Sum
    
def main():

    Data = [10, 15, 20, 25]

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