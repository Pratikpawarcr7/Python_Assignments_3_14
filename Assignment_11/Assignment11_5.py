# ----------------------------------------------------------
# 5. Palindrome Number Check
# Problem:
# Accept one number and check whether it is a palindrome or not.
#
# Example:
# Input : 121
# Output: Palindrome
#
# Explanation:
# Reverse of 121 is 121
# Since the original number and the reversed number are the same,
# the number is a Palindrome.
#
# Examples of Palindrome Numbers:
# 121, 131, 454, 1221, 12321
#
# Examples of Non-Palindrome Numbers:
# 123, 456, 789
# ----------------------------------------------------------

def ChkPalindrome(No):
    Temp = No
    Rev = 0

    while No > 0:
        Digit = No % 10          
        Rev = Rev * 10 + Digit   
        No = No // 10            

    if Temp == Rev:
        return True
    else:
        return False

def main():
    print("Enter the Number")
    Value1 = int(input())

    Ret = ChkPalindrome(Value1)

    if Ret:
        print(f"{Value1} is Palindrome")
    else:
        print(f"{Value1} is Not Palindrome")

if __name__ == "__main__":
    main()
