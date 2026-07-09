# Write a program that accepts one number as input and checks whether it is divisible by both 3 and 5.
# 
# Example:
# Input:
#     15
# Output:
#     Divisible by 3 and 5

def Chk_Divisible(No1):

    if (No1 % 3 == 0 and No1 % 5 == 0):
        return True
    else:
        return False
   
def main():

    print("Enter the Number : ")
    Value1 = int(input())

    Ret = Chk_Divisible(Value1)

    if(Ret == True):
        print(f"{Value1} is Divisible by 3 and 5")
    else:
         print(f"{Value1} is Not Divisible by 3 and 5")

  
if __name__ == "__main__":
    main()