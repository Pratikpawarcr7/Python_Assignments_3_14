# ----------------------------------------------------------
# 2. Print Factors of a Number
# Problem:
# Accept one number and print all its factors.
#
# Example:
# Input : 12
# Output: 1 2 3 4 6 12
#
# Explanation:
# A factor is a number that divides the given number exactly
# without leaving any remainder.
#
# Factors of 12:
# 1, 2, 3, 4, 6, 12
# ----------------------------------------------------------
def Chk_Factors(No):

    iCnt = 0
    print(f"Factors of {No} is")
    for iCnt in range(1,No+1):
        if(No % iCnt == 0):
            print(iCnt)

def main():
    Value = 0
    print("Enter The Number : ")
    Value = int(input())
                
    Chk_Factors(Value)

if __name__ == "__main__":
    main()