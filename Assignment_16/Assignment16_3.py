# ----------------------------------------------------------
# 3. Function Add()
# Problem:
# Accept two numbers and return their addition.
#
# Example:
# Input : 11 5
# Output: 16
# ----------------------------------------------------------

def Addition(No1,No2):

    Ans = 0
    Ans = No1 + No2
    return Ans

def main():

    print("Enter the First Number : ")
    Value1 = int(input())

    print("Enter the Second Number : ")
    Value2 = int(input())

    Ret = Addition(Value1,Value2)

    print("Addition : ",Ret)


if __name__ == "__main__":
    main()