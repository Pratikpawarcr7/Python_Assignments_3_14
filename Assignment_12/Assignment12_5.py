# Accept one number and print numbers from that number
# down to 1.
#
# Example:
# Input : 5
# Output: 5 4 3 2 1
#
# Explanation:
# Start from the entered number and print numbers
# in decreasing order until 1.
# ----------------------------------------------------------

def Print_Rev_Numbers(iNo):

    iCnt = 0
    print("Numbers Are :- ")
    for iCnt in range(iNo,0,-1):
        print(iCnt)
        
def main():
    print("Enter the Numbers : ")
    iValue = int(input())

    Print_Rev_Numbers(iValue)

if __name__ == "__main__":
    main()