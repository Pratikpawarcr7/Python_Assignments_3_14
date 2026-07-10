# ----------------------------------------------------------
# 4. Lambda Function using reduce()
# Problem:
# Accept a list of numbers and return the addition
# (sum) of all elements.
#
# Example:
# Input : [10, 20, 30]
# Output: 60
#
# Explanation:
# 10 + 20 + 30 = 60
# ----------------------------------------------------------
from functools import reduce
Addition = lambda No1,No2 : No1 + No2
def main():

    Number = list()

    print("How Many Numbers you Want in your List : ")
    Value1 = int(input())

    print("Enter the Members of List : ")

    for iCnt in range(Value1):
        iValue2 = int(input())
        Number.append(iValue2)

    print("Your Input List is :",Number)

    R_Data = reduce(Addition,Number)

    print("Your Input List After Reduce :",R_Data)

if __name__ == "__main__":
    main()
