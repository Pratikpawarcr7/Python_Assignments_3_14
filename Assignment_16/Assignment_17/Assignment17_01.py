# ----------------------------------------------------------
# 1. Arithmetic Module
# Problem:
# Create a module named Arithmetic containing
# four functions:
#
# Add()  -> Addition
# Sub()  -> Subtraction
# Mult() -> Multiplication
# Div()  -> Division
#
# Accept two numbers from the user and call all
# functions from the Arithmetic module.
# ----------------------------------------------------------

from Assignment17_01_1 import *

def Display():
    
   print("Enter the First Number")
   Value1 = int(input())

   print("Enter the First Number")
   Value2 = int(input())

   Ret = Addition(Value1,Value2)
   print(f"Addition : {Ret}")

   Ret = Substraction(Value1,Value2)
   print(f"Substraction : {Ret}")

   Ret = Multiplication(Value1,Value2)
   print(f"Multiplication : {Ret}")

   Ret = Division(Value1,Value2)
   print(f"Division : {Ret}")


def main():
    
    Display()

if __name__ == "__main__":
    main()