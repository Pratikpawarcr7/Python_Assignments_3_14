# ----------------------------------------------------------
# 1. Area of Rectangle
# Problem:
# Accept the length and width of a rectangle and
# print its area.
#
# Formula:
# Area = Length × Width
#
# Example:
# Input :
# Length = 10
# Width  = 5
#
# Output:
# 50
#
# Explanation:
# Area = 10 × 5 = 50
# ----------------------------------------------------------

def Area_of_Rectangle(No1,No2):

    Ans = No1 * No2
    return Ans

def main():
    print("Enter the Length of Rectangle")
    Length = int(input())

    print("Enter the Width of Rectangle")
    Width = int(input())

    Ret = Area_of_Rectangle(Length,Width)

    print(f"Area_of_Rectangle is : {Ret}")

if __name__ == "__main__":
    main()
