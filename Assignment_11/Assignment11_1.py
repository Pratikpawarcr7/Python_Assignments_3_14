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

def Even_Number(No):
    iCnt = 0
    
    for iCnt in range(1,No):
        if(No % iCnt == 0):
            return False
        else:
            return True

def main():
    print("Enter the Number")
    Value1 = int (input())

    Ret = Even_Number(Value1)

    if(Ret == True):
        print(f"{Value1} is Prime Number")
    else:
         print(f"{Value1} is Not Prime Number")

if __name__ == "__main__":
    main()