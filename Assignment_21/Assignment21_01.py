# ----------------------------------------------------------
# 1. Threading - Prime and NonPrime
# Problem:
# Design a Python application that creates two
# threads named Prime and NonPrime.
#
# Both threads should accept a list of integers.
#
# Prime Thread:
# Display all prime numbers from the list.
#
# NonPrime Thread:
# Display all non-prime numbers from the list.
#
# Example:
# Input :
# [11, 4, 13, 8, 17, 20]
#
# Prime Numbers:
# 11 13 17
#
# Non-Prime Numbers:
# 4 8 20
# ----------------------------------------------------------

import time
import threading
import os

def Chk_Prime(numbers):
    print(f"Prime ID :",threading.get_ident())
    primes = []
    for num in numbers:
        if num <= 1:
            continue
        isPrime = True  
        for i in range(2, num):
            if num % i == 0:
                isPrime = False   
                break
        if isPrime:   
            primes.append(num)
    print("Prime numbers are:", primes)

def Check_NonPrime(numbers):
    print(f"NonPrime ID :",threading.get_ident())
    nonprimes = []
    for num in numbers:
        if num <= 1:
            nonprimes.append(num)
            continue
        isPrime = True
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break
        if not isPrime:
            nonprimes.append(num)
    print("Non Prime numbers are:",  nonprimes )

def main():

   Reasult = []

   print("How Many Elements you Want in Yor List : ")
   iValue1 = int(input())

   print("Enter the Members of List : ")

   for iCnt in range(0,iValue1):
       iValue2 = int(input())
       Reasult.append(iValue2)
 
   print("You Input List : ")
   print(Reasult)

   t1 = threading.Thread(target=Chk_Prime,args=(Reasult,))
   t2 = threading.Thread(target=Check_NonPrime,args=(Reasult,))
   
   t1.start()
   t2.start()

   t1.join()
   t2.join()

if __name__ == "__main__":
    main()