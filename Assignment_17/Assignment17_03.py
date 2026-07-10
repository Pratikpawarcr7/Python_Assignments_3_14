# ----------------------------------------------------------
# 3. Factorial of a Number
# Problem:
# Accept one number from the user and return its factorial.
#
# Example:
# Input : 5
# Output: 120
#
# Explanation:
# 5! = 1 × 2 × 3 × 4 × 5 = 120
# ----------------------------------------------------------

def Factorial(No):

    Fact = 1
    for iCnt in range(1,No+1):
        Fact = Fact * iCnt
    return Fact


def main():
    print("Enter the Number : ")
    Value1 = int(input())

    Ret = Factorial(Value1)

    print(f"Factorials Are :{Ret}")

if __name__ == "__main__":
    main()