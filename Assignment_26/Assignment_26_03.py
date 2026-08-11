# ==========================================================
# 3. Arithmetic Class
# ==========================================================
# Problem:
# Write a Python program to implement a class named
# Arithmetic with the following characteristics:
#
# 1. The class should contain two instance variables:
#    Value1 and Value2.
#
# 2. Define a constructor __init__() that initializes
#    all instance variables to 0.
#
# 3. Implement the following instance methods:
#
#    Accept()
#    - Accepts values for Value1 and Value2 from the user.
#
#    Addition()
#    - Returns the addition of Value1 and Value2.
#
#    Subtraction()
#    - Returns the subtraction of Value1 and Value2.
#
#    Multiplication()
#    - Returns the multiplication of Value1 and Value2.
#
#    Division()
#    - Returns the division of Value1 and Value2.
#    - Handle division by zero properly.
#
# 4. Create multiple objects of the Arithmetic class and
#    invoke all the instance methods.
#
# ==========================================================

class Arithmetic:

    def __init__(self):
       
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first value: "))
        self.Value2 = int(input("Enter second value: "))

    def Addition(self):
        return self.Value1 + self.Value2

    def Subtraction(self):
        return self.Value1 - self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2

    def Division(self):
       
        if self.Value2 == 0:
            return "Division by zero is not possible"
        else:
            return self.Value1 / self.Value2

def main():

    obj1 = Arithmetic()
    
    obj1.Accept()
    
    print("Addition :", obj1.Addition())
    print("Subtraction :", obj1.Subtraction())
    print("Multiplication :", obj1.Multiplication())
    print("Division :", obj1.Division())
    
    obj2 = Arithmetic()
    
    obj2.Accept()
    
    print("Addition :", obj2.Addition())
    print("Subtraction :", obj2.Subtraction())
    print("Multiplication :", obj2.Multiplication())
    print("Division :", obj2.Division())

if __name__ == "__main__":
    main()
