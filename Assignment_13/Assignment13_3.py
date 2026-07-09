def Perfect_Numbers(No):

    Sum = 0

    for iCnt in range(1,No - 1):
        if(No % iCnt == 0):
            Sum = Sum + iCnt

    if(Sum == No):
        return True
    else:
        return False

def main():
    print("Enter the Number : ")
    Value = int(input())

    Ret = Perfect_Numbers(Value)

    if(Ret == True):
        print(f"{Value} is Perfect Number ")
    else:
        print(f"{Value} is Not Perfect Number ")


if __name__ == "__main__":
    main()