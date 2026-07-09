# ----------------------------------------------------------
# 8. Lambda Function using filter()
# Problem:
# Accept a list of numbers and return a list of numbers
# divisible by both 3 and 5.
#
# Example:
# Input : [10, 15, 18, 30, 45]
# Output: [15, 30, 45]
# ----------------------------------------------------------

Chk_Divisible = lambda No : (No % 3 == 0) and (No % 5 == 0) 
def main():

    Number = list()

    print("How Many Numbers you Want in your List : ")
    Value1 = int(input())

    print("Enter the Members of List : ")

    for iCnt in range(Value1):
        iValue2 = int(input())
        Number.append(iValue2)

    print("Your Input List is :",Number)

    F_Data = list(filter(Chk_Divisible ,Number))

    print("Your Input List After Filter :",F_Data)

if __name__ == "__main__":
    main()
