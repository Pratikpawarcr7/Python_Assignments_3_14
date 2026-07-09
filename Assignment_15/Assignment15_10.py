# ----------------------------------------------------------
# 10. Lambda Function using filter()
# Problem:
# Accept a list of numbers and return the count
# of even numbers.
#
# Example:
# Input : [1, 2, 3, 4, 5, 6]
# Output: 3
#
# Explanation:
# Even numbers are: 2, 4, 6
# Count = 3
# ----------------------------------------------------------

Chk_Even = lambda No : (No % 2 == 0)
def main():

    Number = list()

    print("How Many Numbers you Want in your List : ")
    Value1 = int(input())

    print("Enter the Members of List : ")

    for iCnt in range(Value1):
        iValue2 = int(input())
        Number.append(iValue2)

    print("Your Input List is :",Number)

    F_Data = list(filter(Chk_Even,Number))

    print("Your Input List After Filter :",F_Data)

if __name__ == "__main__":
    main()
