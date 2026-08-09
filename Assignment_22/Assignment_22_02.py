# ----------------------------------------------------------
# 2. Factorial of Multiple Numbers using Pool.map()
#
# Problem:
# Calculate factorials of multiple numbers simultaneously
# using Pool.map().
#
# Input:
# [10, 15, 20, 25]
#
# Output:
#
# Input Number : 10
# Factorial    : 3628800
#
# Input Number : 15
# Factorial    : 1307674368000
#
# Input Number : 20
# Factorial    : 2432902008176640000
#
# Input Number : 25
# Factorial    : 15511210043330985984000000
#
# Also display the Process ID for each calculation.
# ----------------------------------------------------------

import time
import os
import multiprocessing

def Sum_Of_Square(No):
  
    Sum = 1
    for i in range(1,No+1):
        Sum = Sum * i

    print(f"Pocess is Runnining with P_ID : {os.getpid()} ,Input {No},Factorial:{Sum}")
    

    return Sum

def main():

    Data = [10, 15, 20, 25]
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