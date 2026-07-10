# ----------------------------------------------------------
# 4. filter(), map() and reduce()
# Problem:
# Accept a list of numbers from the user.
#
# Step 1:
# Filter all even numbers from the list.
#
# Step 2:
# Calculate the square of each even number using map().
#
# Step 3:
# Return the addition of all squared numbers using reduce().
#
# Example:
# Input List :
# [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
#
# List after filter :
# [2, 4, 4, 2, 8, 10]
#
# List after map :
# [4, 16, 16, 4, 64, 100]
#
# Output :
# 204
#
# Explanation:
# 4 + 16 + 16 + 4 + 64 + 100 = 204
# ----------------------------------------------------------

from functools import reduce

Even_Number = lambda No1 : No1 % 2 == 0

Even_Square = lambda No1 : No1**2

Square_Addition = lambda No1,No2 : No1 + No2

def main():

    Data = []
    print("How Many Elments you Want in Your List : ")
    Value1 = int(input())

    print("Enter The Elements : ")

    for iCnt in range(0,Value1):
        iValue2 = int(input())
        Data.append(iValue2)

    print("Your Input List is : ",Data)

    F_Data = list(filter(Even_Number,Data))

    print("Your Input List After Filter : ",F_Data)

    M_Data = list(map(Even_Square,F_Data))

    print("Your Input List After Mapping : ",M_Data)

    R_Data = reduce(Square_Addition ,M_Data)

    print("Your Input List After Reduce : ",R_Data)


if __name__ == "__main__":
    main()
