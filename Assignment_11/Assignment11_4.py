# ----------------------------------------------------------
# 4. Reverse a Number
# Problem:
# Accept one number and print the reverse of that number.
#
# Example:
# Input : 123
# Output: 321
#
# Explanation:
# Digits of 123 are 1, 2, 3
# Reversing them gives 3, 2, 1
# Therefore, the reverse number is 321
# ----------------------------------------------------------

def Sum_Digit(No):
    
    Sum = 0
    
    print("Reversing of Number : ")
    while(No > 0):
        Digit = No % 10
        print(Digit)
        No = No // 10

def main():
    print("Enter the Number")
    Value1 = int (input())

    Sum_Digit(Value1)

if __name__ == "__main__":
    main()