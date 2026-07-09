
# ----------------------------------------------------------
# 9. Lambda Function to Return Multiplication of Two Numbers
#
# Example:
# Input : 10 20
# Output: 200
# ----------------------------------------------------------
Multiplication = lambda No1,No2:No1 * No2

def main():
    print("Enter the First Number : ")
    Value1 = int(input())

    print("Enter the Second Number : ")
    Value2 = int(input())

    Ret = Multiplication(Value1,Value2)
    print(f"Multiplication : {Ret}")

if __name__ == "__main__":
    main()