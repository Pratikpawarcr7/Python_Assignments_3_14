# ----------------------------------------------------------
# 3. Lambda Function to Return Maximum of Two Numbers
#
# Example:
# Input : 10 20
# Output: 20
# ----------------------------------------------------------

Max = lambda No1 , No2: No1 if No1 > No2 else No2

def main():
    print("Enter First Number : ")
    Value1 = int(input())

    print("Enter Second Number : ")
    Value2 = int(input())

    Maximum = Max(Value1,Value2)
    print(f"Maximum Number is : {Maximum}")

if __name__ == "__main__":
    main()
