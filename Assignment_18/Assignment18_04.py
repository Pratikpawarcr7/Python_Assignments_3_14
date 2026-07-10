# ----------------------------------------------------------
# 4. Frequency of a Number
# Problem:
# Accept N numbers from the user and store them in a List.
# Accept one more number from the user and return the
# frequency of that number in the List.
#
# Example:
# Input :
# Number of elements : 11
# Elements : 13 5 45 7 4 56 5 34 2 5 65
# Number to search : 5
#
# Output:
# 3
#
# Explanation:
# Number 5 appears 3 times in the List.
# ----------------------------------------------------------

def Min_Element(iLength,Members):

    Sum = 0
    iMin = Members[0]
    for iCnt in range(0,iLength):
        if(iMin > Members[iCnt]):
            iMin = Members[iCnt]
        
        return iMin

def main():
    Elements = []

    print("How Many Members You Want in Your List : ")
    iValue1 = int(input())

    print("Enter the Elements : ")
    
    for iCnt in range(0,iValue1):
        iValue2 = int(input())
        Elements.append(iValue2)

    print("Your Input List is : ",Elements)

    Ret = Min_Element(iValue1,Elements)

    print("Maximum is : ",Ret)

if __name__ == "__main__":
    main()