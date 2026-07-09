# ----------------------------------------------------------
# 9. Count Digits in a Number
# Problem:
# Accept one number and print the count of digits in that number.
#
# Example:
# Input : 7521
# Output: 4
#
# Explanation:
# Digits are 7, 5, 2, 1
# Total digits = 4
# ----------------------------------------------------------

def CountX(No):
    
    Count = 0
    

    while(No > 0):
        Digit = No % 10
        Count = Count + 1
        No = No // 10

    return Count

def main():
    print("Enter the Number")
    Value1 = int (input())

    Ret = CountX(Value1)

    print("count of digits is : ",Ret)

if __name__ == "__main__":
    main()