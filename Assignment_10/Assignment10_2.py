# Question 2:
# Write a program that accepts one number as input and prints the sum of the first N natural numbers.
# Example:
# Input: 5
#
# Output:
#     15

def Summation(No):

    iCnt = 0
    Sum = 0

    for iCnt in range(1,No + 1):
        Sum = Sum + iCnt
    
    return Sum

def main():
    print("Enter the Number : ")
    Value = int(input())

    Ret = Summation(Value)

    print(f"sum of the first {Value} natural numbers is {Ret} ")


if __name__ == "__main__":
    main()