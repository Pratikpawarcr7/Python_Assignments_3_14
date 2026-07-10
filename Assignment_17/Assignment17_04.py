# ----------------------------------------------------------
# 4. Addition of Factors
# Problem:
# Accept one number from the user and return
# the addition of its factors.
#
# Example:
# Input : 12
# Output: 16
#
# Explanation:
# Factors of 12 are:
# 1, 2, 3, 4, 6
#
# Sum = 1 + 2 + 3 + 4 + 6 = 16
# ----------------------------------------------------------

def Factorial(No):

    Sum = 0
    for iCnt in range(1,No):
       if(No % iCnt == 0):
           Sum = Sum + iCnt

    return Sum


def main():
    print("Enter the Number : ")
    Value1 = int(input())

    Ret = Factorial(Value1)

    print(f"Addition of Factorials Are : {Ret}")

if __name__ == "__main__":
    main()