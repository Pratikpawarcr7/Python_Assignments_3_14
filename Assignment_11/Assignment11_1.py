# ----------------------------------------------------------
# 8. Prime Number Check
# Problem:
# Accept one number and check whether it is prime or not.
#
# Example:
# Input : 11
# Output: Prime Number
#
# Explanation:
# A prime number has exactly two factors:
# 1 and itself.
# ----------------------------------------------------------

def CheckPrime(No):

    if No <= 1:
        return False

    for iCnt in range(2, No):
        if (No % iCnt == 0):
            return False
        else:
            return True

def main():

    print("Enter the Number : ")
    Value = int(input())

    Ret = CheckPrime(Value)

    if (Ret == True):
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")

if __name__ == "__main__":
    main()
