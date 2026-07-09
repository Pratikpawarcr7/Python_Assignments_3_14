# Write a program that contains one function named ChkGreater() which accepts two numbers as input and prints the greater number.

# Input:
#     10
#     20
# 
# Output:
#     20 is greater

def ChkGreater(No1,No2):
    if(No1 >= No2):
        return No1
    else:
        return No2

def main():

    print("Enter the First Number : ")
    Value1 = int(input())

    print("Enter the Second Number : ")
    Value2 = int(input())

    Ret = ChkGreater(Value1,Value2)

    print(f"{Ret} Is Greater")


if __name__ == "__main__":
    main()