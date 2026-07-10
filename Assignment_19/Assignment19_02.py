# ----------------------------------------------------------
# 2. Lambda Function - Multiplication
# Problem:
# Write a program which contains one lambda function
# that accepts two parameters and returns their
# multiplication.
#
# Example:
# Input : 4 3
# Output: 12
#
# Input : 6 3
# Output: 18
# ----------------------------------------------------------

Multiplication = lambda No1,No2: No1*No2

def main():
    print("Enter the Number : ")
    Value1 = int(input())

    print("Enter the Number : ")
    Value2 = int(input())

    Ret = Multiplication(Value1,Value2)

    print("Output : ",Ret)

if __name__ == "__main__":
    main()
