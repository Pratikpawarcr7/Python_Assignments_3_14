# ----------------------------------------------------------
# 7. Check Divisibility by 5
# Problem:
# Accept one number and return True if the number
# is divisible by 5, otherwise return False.
#
# Example:
# Input : 8
# Output: False
#
# Input : 25
# Output: True
# ----------------------------------------------------------

def Chk_Divisible(No1):

    if (No1 % 5 == 0):
        return True
    else:
        return False
   
def main():

    print("Enter the Number : ")
    Value1 = int(input())

    Ret = Chk_Divisible(Value1)

    if(Ret == True):
        print("True")
    else:
         print("False")

  
if __name__ == "__main__":
    main()
