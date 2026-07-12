# ----------------------------------------------------------
# 5. Threading Synchronization - Thread1 and Thread2
# Problem:
# Design a Python application that creates two
# threads named Thread1 and Thread2.
#
# Thread1:
# Display numbers from 1 to 50.
#
# Thread2:
# Display numbers from 50 to 1 in reverse order.
#
# Condition:
# Thread2 should start execution only after
# Thread1 has completed its execution.
#
# Use appropriate thread synchronization
# (join() method).
#
# Output:
#
# Thread1:
# 1 2 3 4 5 ... 50
#
# Thread2:
# 50 49 48 47 ... 1
# ----------------------------------------------------------

import time
import threading
def Display_No(No):

    Result = []
    iCnt = 0 
    for iCnt in range(1,No + 1,1):
        Result.append(iCnt)

    print("Thread1 : ")
    print(Result)

def Display_No_Rev(No):

    Result = []
    iCnt = 0 
    for iCnt in range(No,0,-1):
        Result.append(iCnt)

    print("Thread1 : ")
    print(Result)
    


def main():

    start_time = time.perf_counter()

    Thread_1 = threading.Thread(target = Display_No,args = (50,))
    Thread_1.start()
    Thread_1.join()

    Thread_2 = threading.Thread(target = Display_No_Rev,args = (50,))
    Thread_2.start()
    Thread_2.join()

    end_time = time.perf_counter()

    print(f"Require Time : {end_time - start_time:.4f}")


if __name__ == "__main__":
    main()