# ----------------------------------------------------------
# 8. Lambda Function to Return Addition of Two Numbers
#
# Example:
# Input : 10 20
# Output: 30
# ----------------------------------------------------------
Addition = lambda No1,No2:No1 + No2

def main():
    print("Enter the First Number : ")
    Value1 = int(input())

    print("Enter the Second Number : ")
    Value2 = int(input())

    Ret = Addition(Value1,Value2)
    print(f"Addition : {Ret}")

if __name__ == "__main__":
    main()
