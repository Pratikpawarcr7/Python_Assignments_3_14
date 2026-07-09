
# ----------------------------------------------------------
# 4. Binary Equivalent
# Problem:
# Accept one number and print its binary equivalent.
#
# Example:
# Input : 10
#
# Output:
# 1010
#
# Explanation:
# Binary is a number system that uses only
# two digits: 0 and 1.
#
# Decimal 10 in Binary:
#
# 10 ÷ 2 = 5  Remainder 0
#  5 ÷ 2 = 2  Remainder 1
#  2 ÷ 2 = 1  Remainder 0
#  1 ÷ 2 = 0  Remainder 1
#
# Reading remainders from bottom to top:
# 1010
#
# Therefore:
# Binary Equivalent of 10 is 1010
# ----------------------------------------------------------

# Program: Binary Equivalent

def decimal_to_binary(number):
    return bin(number).replace("0b", "")

def main():
    print("Enter a Number: ")
    num = int(input())
    
    binary = decimal_to_binary(num)
    print(f"Binary Equivalent of {num} is: {binary}")

if __name__ == "__main__":
    main()
