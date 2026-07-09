# Question 3:
# Write a program that accepts one number as input and prints the square of that number.
# 
# Example:
# Input:
#         5
# Output:
#     25

def Chk_Square(No1):

    Square = (No1**2)
    return Square
   

def main():

    print("Enter the Number : ")
    Value1 = int(input())

    Ret = Chk_Square(Value1)

    print(f"Square of {Value1} is {Ret}")


if __name__ == "__main__":
    main()