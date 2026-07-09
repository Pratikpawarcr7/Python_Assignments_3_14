# Question 3:
# 
# Write a program that accepts one number as input and prints the factorial of that number.
# 
# Example:
# 
# Input: 5
# 
# Output: 120

def Factorial(No):

    iCnt = 0
    fAct = 1

    for iCnt in range(1,No + 1):
        fAct = fAct * iCnt
    
    return fAct

def main():
    print("Enter the Number : ")
    Value = int(input())

    Ret = Factorial(Value)

    print(f"Factorial of {Value} is {Ret} ")


if __name__ == "__main__":
    main()