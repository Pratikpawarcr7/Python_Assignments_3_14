# ----------------------------------------------------------
# 1. Lambda Function using map()
# Problem:
# Accept a list of numbers and return a list containing
# the square of each number.
#
# Example:
# Input : [1, 2, 3, 4]
# Output: [1, 4, 9, 16]
# ----------------------------------------------------------
Chk_Square = lambda No : (No**2)
def main():

    Number = list()

    print("How Many Numbers you Want in your List : ")
    Value1 = int(input())

    print("Enter the Members of List : ")

    for iCnt in range(Value1):
        iValue2 = int(input())
        Number.append(iValue2)

    print("Your Input List is :",Number)

    M_Data = list(map(Chk_Square,Number))

    print("Your Input List After Mapping :",M_Data)

if __name__ == "__main__":
    main()
