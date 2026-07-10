# ----------------------------------------------------------
# 10. Sum of Digits
# Problem:
# Accept one number from the user and return
# the addition (sum) of digits in that number.
#
# Example:
# Input : 5187934
# Output: 37
#
# Explanation:
# 5 + 1 + 8 + 7 + 9 + 3 + 4 = 37
# ----------------------------------------------------------

def Display(No):

  
    Digit = 1
    Sum = 0

    while(No > 0):

        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():

    print("Enter the Number : ")
    Value = int(input())

    Ret = Display(Value)

    print("Summation : ",Ret)

if __name__ == "__main__":
    main()