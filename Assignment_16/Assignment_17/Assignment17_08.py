# ----------------------------------------------------------
# 8. Pattern Printing
# Problem:
# Accept one number and display the following pattern.
#
# Input : 5
#
# Output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# ----------------------------------------------------------

def Display(Row,Col):

    if(Row != Col):
        return
    
    for rCnt in range(1,Row + 1):
        for cCnt in range(1,rCnt + 1):
          
                print(cCnt,end=" ")

        print()

def main():
    print("Enter the Number of Rows")
    iValue1 = int(input())

    print("Enter the Number of Colums")
    iValue2 = int(input())

    Display(iValue1,iValue2)

if __name__ == "__main__":
    main()