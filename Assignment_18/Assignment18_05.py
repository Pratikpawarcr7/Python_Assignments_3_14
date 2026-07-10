# ----------------------------------------------------------
# 5. Addition of Prime Numbers from List
# Problem:
# Accept N numbers from the user and store them in a List.
# Return the addition of all prime numbers from that List.
#
# Main Python file should accept N numbers from user and
# pass each number to ChkPrime() function which is part of
# user-defined module MarvellousNum.
#
# Function name in main Python file:
# ListPrime()
#
# Example:
# Input :
# Number of elements : 11
# Elements : 13 5 45 7 4 56 10 34 2 5 8
#
# Output:
# 32
#
# Explanation:
# Prime Numbers are:
# 13, 5, 7, 2, 5
#
# Sum = 13 + 5 + 7 + 2 + 5 = 32
# ----------------------------------------------------------

def Min_Element(iLength,Freq,Members):

    Count = 0
    
    for iCnt in range(0,iLength):
        if(Freq == Members[iCnt] ):
            Count = Count + 1
        
    return Count

def main():
    Elements = []

    print("How Many Members You Want in Your List : ")
    iValue1 = int(input())

    print("Enter the Elements : ")
    
    for iCnt in range(0,iValue1):
        iValue2 = int(input())
        Elements.append(iValue2)

    print("Enter the Number that you Want to Find Frequency of that Number : ")
    iValue2 = int(input())

    print("Your Input List is : ",Elements)

    Ret = Min_Element(iValue1,iValue2,Elements)

    print("Frequency of that Number is : ",Ret)

if __name__ == "__main__":
    main()