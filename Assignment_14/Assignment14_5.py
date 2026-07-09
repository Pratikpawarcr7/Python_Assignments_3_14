# ----------------------------------------------------------
# 5. Lambda Function to Check Even Number
#
# Example:
# Input : 8
# Output: True
#
# Input : 7
# Output: False
#
# Explanation:
# Return True if the number is even,
# otherwise return False.
# ----------------------------------------------------------

Even = lambda No1 : True if No1 % 2 == 0 else False

def main():
    print("Enter First Number : ")
    Value1 = int(input())

    Chk_Even = Even(Value1)
    print(f"{Chk_Even }")

if __name__ == "__main__":
    main()