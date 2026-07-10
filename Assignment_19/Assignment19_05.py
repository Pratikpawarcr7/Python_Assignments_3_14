# ----------------------------------------------------------
# 5. filter(), map() and reduce()
# Problem:
# Write a program which contains filter(), map(),
# and reduce() functions.
#
# The application accepts a list of numbers from the user.
#
# Step 1:
# Filter all prime numbers from the list.
#
# Step 2:
# Multiply each prime number by 2 using map().
#
# Step 3:
# Return the maximum number from the mapped list
# using reduce().
#
# (You can also use normal functions instead of
# lambda functions.)
#
# Example:
# Input List :
# [2, 70, 11, 10, 17, 23, 31, 77]
#
# List after filter :
# [2, 11, 17, 23, 31]
#
# List after map :
# [4, 22, 34, 46, 62]
#
# Output :
# 62
#
# Explanation:
# Prime numbers are:
# 2, 11, 17, 23, 31
#
# After multiplying each by 2:
# 4, 22, 34, 46, 62
#
# Maximum number = 62
# ----------------------------------------------------------


Check_Prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

Multiplication = lambda No1 : No1 * 2

Maximum = lambda No1,No2 : No1 if No1 > No2 else No2

def filterX(Task,Elements):

    Result = []

    for iCnt in Elements:

        Ret = Task(iCnt)

        if(Ret == True):
            Result.append(iCnt)
    return Result

def mapX(Task,Elements):

    Result = []

    for iCnt in Elements:

        Ret = Task(iCnt)
        Result.append(Ret)

    return Result

def reduceX(Task,Elements):
   
   Max = 0
   for iCnt in Elements:
        Max = Task(Max,iCnt)
        
   return Max

def main():

    Marvellous = []

    print("How Many Members You Want in Your List : ")
    iValue1 = int(input())

    print("Enter the Number : ")

    for iCnt in range(0,iValue1):
        iValue2 = int(input())

        Marvellous.append(iValue2)

    print("Your Input List : ")
    print(Marvellous)    

    F_Data = list(filterX(Check_Prime,Marvellous))
    print("Input List After Filter : ")
    print(F_Data)

    M_Data = list(mapX(Multiplication,F_Data))
    print("Input List After Mapping : ")
    print(M_Data)

    R_Data = reduceX(Maximum,M_Data)
    print("Input List After Reduce : ")
    print(R_Data)


if __name__ == "__main__":
    main()