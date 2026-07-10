# ----------------------------------------------------------
# 6. Pattern Printing
# Problem:
# Accept one number and display the following pattern.
#
# Input : 5
#
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
# ----------------------------------------------------------

def Display(Row,Col):

    if(Row != Col):
        return
    
    for rCnt in range(Row,0,-1):
        for cCnt in range(rCnt):
           print("*",end=" ")

        print()

def main():
    print("Enter the Number of Rows")
    iValue1 = int(input())

    print("Enter the Number of Colums")
    iValue2 = int(input())

    Display(iValue1,iValue2)

if __name__ == "__main__":
    main()