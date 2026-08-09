# ----------------------------------------------------------
# 3. Count Prime Numbers using Multiprocessing Pool
#
# Problem:
# For every number in the given list, count how many
# prime numbers exist between 1 and N using multiprocessing
# Pool.
#
# Input:
# [10000, 20000, 30000, 40000]
#
# Output:
#
# Number : 10000
# Prime Count : 1229
#
# Number : 20000
# Prime Count : 2262
#
# Number : 30000
# Prime Count : 3245
#
# Number : 40000
# Prime Count : 4203
# ----------------------------------------------------------
import os
import multiprocessing
import time


def CheckPrime(No):

    if No <= 1:
        return False

    for Cnt in range(2, No):
        if No % Cnt == 0:
            return False

    return True


def Count_Prime(No):

    Count = 0

    for Cnt in range(1, No + 1):

        if CheckPrime(Cnt):
            Count = Count + 1

    print(f"Process is Running with P_ID : {os.getpid()}, "
          f"Input : {No}, Prime Count : {Count}")

    return Count


def main():

    Data = [10000, 20000, 30000, 40000]

    Start_Time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Result = pobj.map(Count_Prime, Data)

    pobj.close()
    pobj.join()

    End_Time = time.perf_counter()

    print("\nResult :", Result)

    print(f"Time Required : {End_Time - Start_Time:.4f} seconds")


if __name__ == "__main__":
    main()