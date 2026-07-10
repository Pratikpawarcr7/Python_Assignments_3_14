# ----------------------------------------------------------
# 2. Pattern Printing
# Problem:
# Accept one number and display the following pattern.
#
# Input : 5
#
# Output:
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# ----------------------------------------------------------

def Display_Star(No1,No2):

    if (No1 != No2):
        print("Invalid OutPut")
        return 

    print("Output : ")

    for rCnt in range(1,No1+1):
        for cCnt in range(1,No2+1):
            print("*",end=" ") 
        print()

def main():

    print("Enter First Number :")
    Value1 = int(input())

    print("Enter Second Number :")
    Value2 = int(input())

    Display_Star(Value1,Value2)

if __name__ == "__main__":
    main()