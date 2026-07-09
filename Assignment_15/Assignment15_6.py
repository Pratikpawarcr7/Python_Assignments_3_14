# ----------------------------------------------------------
# 6. Lambda Function using reduce()
# Problem:
# Accept a list of numbers and return the minimum element.
#
# Example:
# Input : [10, 50, 20, 40]
# Output: 10
# ----------------------------------------------------------
from functools import reduce
Minimum = lambda No1,No2 : No1 if No1 < No2 else No2
def main():

    Number = list()

    print("How Many Numbers you Want in your List : ")
    Value1 = int(input())

    print("Enter the Members of List : ")

    for iCnt in range(Value1):
        iValue2 = int(input())
        Number.append(iValue2)

    print("Your Input List is :",Number)

    R_Data = reduce(Minimum,Number)

    print("Your Minimum Input Using Reduce :",R_Data)

if __name__ == "__main__":
    main()
