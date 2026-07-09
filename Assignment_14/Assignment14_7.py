# ----------------------------------------------------------
# 7. Lambda Function to Check Divisibility by 5
#
# Example:
# Input : 25
# Output: True
#
# Input : 23
# Output: False
#
# Explanation:
# Return True if the number is divisible by 5,
# otherwise return False.
# ----------------------------------------------------------

Chk_Divisibility = lambda No1 : True if No1 % 5 == 0 else False

def main():
    print("Enter First Number : ")
    Value1 = int(input())

    Chk_Div = Chk_Divisibility(Value1)
    print(f"{Chk_Div}")

if __name__ == "__main__":
    main()