# ==========================================================
# 2. Circle Class
# ==========================================================

# Problem:
# Write a Python program to implement a class named Circle
# with the following specifications:
#
# 1. The class should contain three instance variables:
#    Radius, Area, and Circumference.
#
# 2. The class should contain one class variable named PI,
#    initialized to 3.14.
#
# 3. Define a constructor __init__() that initializes all
#    instance variables to 0.0.
#
# 4. Implement the following instance methods:
#
#    Accept()
#    - Accepts the radius of the circle from the user.
#
#    CalculateArea()
#    - Calculates the area of the circle and stores it
#      in the Area variable.
#
#    CalculateCircumference()
#    - Calculates the circumference of the circle and stores
#      it in the Circumference variable.
#
#    Display()
#    - Displays the values of Radius, Area, and Circumference.
#
# 5. Create multiple objects of the Circle class and invoke
#    all the instance methods for each object.
#
# Formula:
# Area = PI * Radius * Radius
#
# Circumference = 2 * PI * Radius
#
# Example:
#
# Input:
# Enter radius: 5
#
# Output:
# Radius : 5.0
# Area : 78.5
# Circumference : 31.4
#
# ==========================================================

class Circle:

    PI = 3.14

    def __init__(self):
        self. Radius = 0.0
        self.Area = 0.0 
        self.Circumference = 0.0

    def Accept(self):
          self.Radius = float(input("Enter Radius : "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
            self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
         print("Radius : ",self.Radius)
         print("Area : ",self.Area)
         print("Circumference",self.Circumference)


def main():
    obj1 = Circle()


    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    obj2 = Circle()

    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()

if __name__ == "__main__":
    main()







