# ----------------------------------------------------------
# 4. Lambda Function to Return Minimum of Two Numbers
#
# Example:
# Input : 10 20
# Output: 10
# ----------------------------------------------------------
Min = lambda No1 , No2: No1 if No1 < No2 else No2

def main():
    print("Enter First Number : ")
    Value1 = int(input())

    print("Enter Second Number : ")
    Value2 = int(input())

    Minimum = Min(Value1,Value2)
    print(f"Minimum Number is : {Minimum}")

if __name__ == "__main__":
    main()