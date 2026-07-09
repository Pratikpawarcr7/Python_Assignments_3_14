#----------------------------------------------------------------------------------------------------------------
# Question 1:
#     Write a program that accepts one number as input and prints the multiplication table of that number.
# Example:
#     Input:
#     4
# Output:
#     4 8 12 16 20 24 28 32 36 40
#------------------------------------------------------------------------------------------------------------------

def table(No1):
    print("Tables Are :- ")
    for iCnt in range(1,10+1):
        print(iCnt* No1)
   

def main():

    print("Enter the Number : ")
    Value1 = int(input())

    table(Value1)

if __name__ == "__main__":
    main()