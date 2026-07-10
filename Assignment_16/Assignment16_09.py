# ----------------------------------------------------------
# 9. First 10 Even Numbers
# Problem:
# Display the first 10 even numbers.
#
# Output:
# 2 4 6 8 10 12 14 16 18 20
# ----------------------------------------------------------

def Display_Even(No):

    if(No == 2):
        for iCnt in range(1,11,1):
            print(iCnt*2)
    else:
        print("Please Enter 2 if you want to Display the first 10 even numbers")

def main():

    print("Entre the Number : ")
    Value = int(input())

    Display_Even(Value)

if __name__ == "__main__":
    main()
