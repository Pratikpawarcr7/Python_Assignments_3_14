
# ----------------------------------------------------------
# 10. Lambda Function to Return Largest of Three Numbers
#
# Example:
# Input : 10 20 30
# Output: 30
#
# Explanation:
# Compare all three numbers and
# return the largest one.
# ----------------------------------------------------------

Max = lambda No1, No2, No3: No1 if (No1 > No2 and No1 > No3) else (No2 if No2 > No3 else No3)

def main():

    Large = []
    print("Enter First Number : ")
    Value1 = int(input())

    print("Enter Second Number : ")
    Value2 = int(input())

    print("Enter Third Number : ")
    Value3 = int(input())

    Maximum = Max(Value1,Value2,Value3)
    print(f"Maximum Number is : {Maximum}")

if __name__ == "__main__":
    main()