# ----------------------------------------------------------
# 1. Sum of Squares using multiprocessing Pool.map()
#
# Problem:
# Accept a list of integers and use Pool.map() to calculate
# the sum of squares from 1 to N for every element in the list.
#
# Formula:
# 1² + 2² + 3² + ... + N²
#
# Input:
# [1000000, 2000000, 3000000, 4000000]
#
# Output:
# [333333833333500000,
#  2666668666667000000,
#  9000004500000500000,
#  21333341333334000000]
#
# ----------------------------------------------------------
import time
import os
import multiprocessing

def Sum_Of_Square(No):
    print("Pocess is Runnining with P_ID",os.getpid())
    Sum = 0
    for i in range(1,No+1):
        Sum = Sum + (i**2)

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