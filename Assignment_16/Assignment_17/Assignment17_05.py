# ----------------------------------------------------------
# 5. Prime Number Check
# Problem:
# Accept one number from the user and check
# whether it is prime or not.
#
# Example:
# Input : 5
# Output: It is Prime Number
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