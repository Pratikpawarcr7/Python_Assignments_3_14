# ----------------------------------------------------------
# 1. Lambda Function to Return Square of a Number
#
# Example:
# Input : 5
# Output: 25
# ----------------------------------------------------------

Square = lambda No: (No**2)

def main():
    print("Enter the Number : ")
    Value = int(input())

    Squ_Num = Square(Value)
    print(f"Square of {Value} is : {Squ_Num}")

if __name__ == "__main__":
    main()
