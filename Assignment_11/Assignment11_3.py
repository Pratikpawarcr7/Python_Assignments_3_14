# ----------------------------------------------------------
# 3. Sum of Digits
# Problem:
# Accept one number and print the sum of its digits.
#
# Example:
# Input : 123
# Output: 6
#
# Explanation:
# Digits are 1, 2, and 3
# Sum = 1 + 2 + 3 = 6
# ----------------------------------------------------------

def Sum_Digit(No):
    
    Sum = 0
    

    while(No > 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    print("Enter the Number")
    Value1 = int (input())

    Ret = Sum_Digit(Value1)

    print("Summation of digits is : ",Ret)

if __name__ == "__main__":
    main()