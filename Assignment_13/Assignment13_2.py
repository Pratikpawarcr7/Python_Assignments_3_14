# ----------------------------------------------------------
# 2. Area of Circle
# Problem:
# Accept the radius of a circle and print its area.
#
# Formula:
# Area = π × Radius × Radius
#
# Example:
# Input :
# Radius = 7
#
# Output:
# 153.94
#
# Explanation:
# Area = 3.14 × 7 × 7
#      = 153.86 (approximately)
#
# Note:
# π (Pi) ≈ 3.14
# ----------------------------------------------------------

def  Radius_Of_Circle(RadiusX,PI = 3.14):

    Area = PI * RadiusX * RadiusX
    return Area

def main():
    print("Enter the Radius of Circle : ")
    Radius = float(input())

    Ret =  Radius_Of_Circle(Radius)
    print(f"Area of Circle is {Ret}")

if __name__ == "__main__":
    main()