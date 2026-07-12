# ----------------------------------------------------------
# 3. Threading with Shared Variable and Lock
# Problem:
# Design a Python application where multiple
# threads update a shared variable.
#
# Use a Lock to avoid race conditions.
#
# Each thread should increment the shared
# counter multiple times.
#
# Display the final value of the counter
# after all threads complete execution.
#
# Example:
# Counter Initial Value = 0
#
# Thread1 increments counter 1000 times
# Thread2 increments counter 1000 times
# Thread3 increments counter 1000 times
#
# Final Counter Value = 3000
# ----------------------------------------------------------

import threading

# Shared counter
counter = 0
# Lock object
lock = threading.Lock()

def increment_counter(times):
    global counter
    for _ in range(times):
        # acquire lock before updating shared variable
        lock.acquire()
        counter += 1
        lock.release()

def main():
    global counter
    counter = 0   

    print("Counter Initial Value =", counter)

    
    t1 = threading.Thread(target=increment_counter, args=(1000,), name="Thread1")
    t2 = threading.Thread(target=increment_counter, args=(1000,), name="Thread2")
    t3 = threading.Thread(target=increment_counter, args=(1000,), name="Thread3")

    
    t1.start()
    t2.start()
    t3.start()

    
    t1.join()
    t2.join()
    t3.join()

    print("Final Counter Value =", counter)

if __name__ == "__main__":
    main()
