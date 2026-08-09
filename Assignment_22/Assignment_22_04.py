# ----------------------------------------------------------
# 4. Calculate Fifth-Power Series using Pool
#
# Problem:
# Calculate:
#
# 1⁵ + 2⁵ + 3⁵ + ... + N⁵
#
# for multiple values of N simultaneously using Pool.
#
# Input:
# [1000000, 2000000, 3000000, 4000000]
#
# Output:
#
# N = 1000000
# Sum = 166667166667083333333333250000000000
#
# N = 2000000
# Sum = 10666682666673333333333333000000000000
#
# N = 3000000
# Sum = 121500121500033749999999999250000000000
#
# N = 4000000
# Sum = 682667178666773333333333332000000000000
#
# Also display:
# Total Execution Time
# ----------------------------------------------------------

import time
import os
import multiprocessing

def Sum_Of_Square(No):
    print("Pocess is Runnining with P_ID",os.getpid())
    Sum = 0
    for i in range(1,No+1):
        Sum = Sum + (i**5)

    return Sum

def main():

    Data = [1000000, 2000000, 3000000, 4000000]
    Result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    Result = pobj.map(Sum_Of_Square,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print(Result)
    print(f"Time Require : {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()