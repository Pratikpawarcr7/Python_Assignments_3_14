# ----------------------------------------------------------
# 9. Lambda Function using reduce()
# Problem:
# Accept a list of numbers and return the product
# of all elements.
#
# Example:
# Input : [2, 3, 4]
# Output: 24
#
# Explanation:
# 2 * 3 * 4 = 24
# ----------------------------------------------------------

from functools import reduce
Product = lambda No1,No2 : No1 * No2
def main():

    Number = list()

    print("How Many Numbers you Want in your List : ")
    Value1 = int(input())

    print("Enter the Members of List : ")

    for iCnt in range(Value1):
        iValue2 = int(input())
        Number.append(iValue2)

    print("Your Input List is :",Number)

    R_Data = reduce(Product,Number)

    print("Your Input Using Reduce :",R_Data)

if __name__ == "__main__":
    main()
