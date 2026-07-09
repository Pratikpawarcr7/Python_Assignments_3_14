# ----------------------------------------------------------
# 2. Lambda Function to Return Cube of a Number
#
# Example:
# Input : 5
# Output: 125
# ----------------------------------------------------------


Cube = lambda No: (No**3)

def main():
    print("Enter the Number : ")
    Value = int(input())

    Cube_Num = Cube(Value)
    print(f"Square of {Value} is : {Cube_Num}")

if __name__ == "__main__":
    main()