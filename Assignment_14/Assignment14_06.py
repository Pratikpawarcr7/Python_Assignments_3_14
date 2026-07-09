# ----------------------------------------------------------
# 6. Lambda Function to Check Odd Number
#
# Example:
# Input : 7
# Output: True
#
# Input : 8
# Output: False
#
# Explanation:
# Return True if the number is odd,
# otherwise return False.
# ----------------------------------------------------------


Odd = lambda No1 : True if No1 % 2 != 0 else False

def main():
    print("Enter First Number : ")
    Value1 = int(input())

    Chk_Odd = Odd(Value1)
    print(f"{Chk_Odd}")

if __name__ == "__main__":
    main()
