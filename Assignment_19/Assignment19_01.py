# ----------------------------------------------------------
# 1. Lambda Function - Power of Two
# Problem:
# Write a program which contains one lambda function
# that accepts one parameter and returns its power of two.
#
# Example:
# Input : 4
# Output: 16
#
# Input : 6
# Output: 64
#
# Explanation:
# 4² = 16
# 6² = 64
# ----------------------------------------------------------

Display = lambda No:( No**2 )

def main():
    print("Enter the Number : ")
    Value1 = int(input())

    Ret = Display(Value1)

    print("Output : ",Ret)

if __name__ == "__main__":
    main()
