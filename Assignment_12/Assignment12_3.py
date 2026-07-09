
# ----------------------------------------------------------
#  3. Arithmetic Operations
#  Problem:
#  Accept two numbers and print their:
#  Addition, Subtraction, Multiplication, and Division.
# 
#  Example:
#  Input : 10 5
# 
#  Output:
#  Addition       : 15
#  Subtraction    : 5
#  Multiplication : 50
#  Division       : 2
# ----------------------------------------------------------

def Arithmatic(No1,No2):

    Add = No1 + No2
    Sub = No1 - No2
    Mult = No1 * No2
    Divi = No1 / No2

    return Add,Sub,Mult,Divi
   

def main():
    print("Enter the First Number ")
    Value1 = int(input())

    print("Enter the Second Number ")
    Value2 = int(input())

    Ret1,Ret2,Ret3,Ret4 = Arithmatic(Value1,Value2)

    print("Addition      :",Ret1)

    print("Subtraction   :",Ret2)

    print("Multiplication:",Ret3)

    print("Division      :",Ret4)

if __name__ == "__main__":
    main()