# Question 4:
# Write a program that accepts one number as input and prints all the even numbers till that number.
# 
# Example:
# Input: 10
# 
# Output: 2 4 6 8 10

def Even_Number(No):
    iCnt = 0
    eVen = 0

    print(f" Even Factors of {No} is :")
    for iCnt in range(1,11):
        if(iCnt % 2 == 0):
            print(iCnt)

def main():
    print("Enter the Number")
    iValue = int (input())

    Even_Number(iValue)

if __name__ == "__main__":
    main()