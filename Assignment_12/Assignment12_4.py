# ----------------------------------------------------------
# 4. Print Numbers from 1 to N
# Problem:
# Accept one number and print numbers starting from 1
# up to that number.
#
# Example:
# Input : 5
# Output: 1 2 3 4 5
#
# Explanation:
# Print all numbers from 1 to the entered number.
# ----------------------------------------------------------

def Print_Numbers(iNo):

    iCnt = 0
    print("Numbers Are :- ")
    for iCnt in range(1,iNo+1):
        print(iCnt)
        

def main():
    print("Enter the Numbers : ")
    iValue = int(input())

    Print_Numbers(iValue)

if __name__ == "__main__":
    main()