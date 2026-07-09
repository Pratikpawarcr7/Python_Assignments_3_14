# Question 3:
# Write a program that accepts one number as input and prints the Cude of that number.
# 
# Example:
# Input: 5
# Output: 25

def Chk_Cube(No1):

    Cube = (No1 ** 3)
    return Cube
   
def main():

    print("Enter the Number : ")
    Value1 = int(input())

    Ret = Chk_Cube(Value1)

    print(f"Cube of {Value1} is {Ret}")


if __name__ == "__main__":
    main()