#######################################################################################################
# 
# 1. Write a Python program to implement a class named Demo with the following specifications:
# 
########################################################################################################
#
# The class should contain two instance variables named no1 and no2.
#
# The class should contain one class variable named Value.
# 
# Define a constructor __init__() that accepts two parameters and initializes no1 and no2.
# 
# Define two instance methods:
# 
# Fun() — displays the values of no1 and no2.
# 
# Gun() — displays the values of no1 and no2.
# 
# Create two objects:
# 
# Obj1 = Demo(11, 21)
# Obj2 = Demo(51, 101)
# 
# Call the methods in the following sequence:
# 
# Obj1.Fun()
# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()
# 
#########################################################################################################

class Demo:
    Value1 = 10

    def __init__(self,No1,No2):
        self.No1 = No1
        self.No2 = No2


    def Fun(self):
        print("Value of No1 inside Fun:",self.No1)
        print("Value of No2 inside Fun:",self.No2)

    def Gun(self):
           print("Value of No1 inside Gun:",self.No1)
           print("Value of No2 inside Gun:",self.No2)

def main():
    obj1 = Demo(11,21)
    obj2 = Demo(15,101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()
