# ----------------------------------------------------------
# 3. filter(), map() and reduce()
# Problem:
# Accept a list of numbers from the user.
#
# Step 1:
# Filter all numbers greater than or equal to 70
# and less than or equal to 90.
#
# Step 2:
# Increase each filtered number by 10 using map().
#
# Step 3:
# Return the product of all mapped numbers using reduce().
#
# Example:
# Input List :
# [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
#
# List after filter :
# [76, 89, 86, 90, 70]
#
# List after map :
# [86, 99, 96, 100, 80]
#4
# Output after reduce :
# 6538752000
# ----------------------------------------------------------

from functools import reduce

G_equal = lambda No1 : 70 <= No1 <= 90

Incriment = lambda No1 : No1 + 10

Product = lambda No1,No2 : No1 * No2

def main():

    Data = []
    print("How Many Elments you Want in Your List : ")
    Value1 = int(input())

    print("Enter The Elements : ")

    for iCnt in range(0,Value1):
        iValue2 = int(input())
        Data.append(iValue2)

    print("Your Input List is : ",Data)

    F_Data = list(filter(G_equal,Data))

    print("Your Input List After Filter : ",F_Data)

    M_Data = list(map(Incriment,F_Data))

    print("Your Input List After Mapping : ",M_Data)

    R_Data = reduce(Product,M_Data)

    print("Your Input List After Reduce : ",R_Data)


if __name__ == "__main__":
    main()
