# ----------------------------------------------------------
# 9. Count Digits
# Problem:
# Accept one number from the user and return
# the number of digits in that number.
#
# Example:
# Input : 5187934
# Output: 7
# ----------------------------------------------------------

def Display(No):

  
    Digit = 1
    Count = 0

    while(No > 0):

        Digit = No % 10
        Count = Count + 1
        No = No // 10

    return Count

def main():

    print("Enter the Number : ")
    Value = int(input())

    Ret = Display(Value)

    print("Count : ",Ret)

if __name__ == "__main__":
    main()