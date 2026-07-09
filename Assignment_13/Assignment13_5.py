def Marks(Mark):

    if(Mark >= 75):
        print("Distinction")
    elif(Mark>=60 and Mark<=75):
         print("First Class")
    elif(Mark>=50 and Mark<=60):
        print("Second Class")
    elif(Mark < 50):
        print("Fail")
        

def main():
    print("Enter the Marks : ")
    Value = int(input())

    Marks(Value)

if __name__ == "__main__":
    main()