# ----------------------------------------------------------
# 1. Threading - Even and Odd Numbers
# Problem:
# Design a Python application that creates two
# separate threads named Even and Odd.
#
# Even Thread:
# Display the first 10 even numbers.
#
# Odd Thread:
# Display the first 10 odd numbers.
#
# Both threads should execute independently
# using the threading module.
#
# Ensure proper thread creation and execution.
# ----------------------------------------------------------

import time
import threading


def Even(no):
    print("Even Thread Started")
    for iCnt in range(2,no+1,2):
        if iCnt % 2==0:
            print("first 10 even numbers.",iCnt)
    print("Even Thread Finished")

def Odd(no):
    print("Odd Thread Started")
    for iCnt in range(1,no+1,2):
        if iCnt % 2!=0:
            print("first 10 Odd  numbers.",iCnt)
    print("Odd Thread Finished")


def main():

    
    start_time = time.perf_counter()

    t1 = threading.Thread(target=Even,args =(10,))
    t2 = threading.Thread(target=Odd,args =(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    
    end_time = time.perf_counter()

       
    print(f"Time Required is :{end_time - start_time:.4f}")

if __name__ == "__main__":
    main()

