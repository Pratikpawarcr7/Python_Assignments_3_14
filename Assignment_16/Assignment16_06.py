# ----------------------------------------------------------
# 6. Positive, Negative or Zero
# Problem:
# Accept one number and check whether it is
# positive, negative, or zero.
#
# Example:
# Input : 11
# Output: Positive Number
#
# Input : -8
# Output: Negative Number
#
# Input : 0
# Output: Zero
# ----------------------------------------------------------
def Chk_PNZ(No1):

    if(No1>0):

        print(" Positive Number")

    elif(No1<0):

        print("Negative Number")

    elif(No1 == 0):

        print("Zero")

def main():

    print("Enter the Number : ")
    Value1 = int(input())

    Ret = Chk_PNZ(Value1)

if __name__ == "__main__":
    main()
