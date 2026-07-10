# ----------------------------------------------------------
# 2. Function ChkNum()
# Problem:
# Accept one number and check whether it is even or odd.
#
# Example:
# Input : 11
# Output: Odd Number
#
# Input : 8
# Output: Even Number
# ----------------------------------------------------------

def Chk_Odd_Even(No):

    if(No % 2 == 0):

        return True
    
    else:

        return False
    
def main():
    print("Enter the number : ")
    Value = int(input())

    bRet = Chk_Odd_Even(Value)

    if(bRet == True):

        print("Even Number")

    else:
        
        print("Odd Number")

if __name__ == "__main__":
    main()
