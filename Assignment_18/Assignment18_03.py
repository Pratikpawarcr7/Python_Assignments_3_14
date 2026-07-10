# ----------------------------------------------------------
# 3. Minimum Number from List
# Problem:
# Accept N numbers from the user and store them in a List.
# Return the minimum number from that List.
#
# Example:
# Input :
# Number of elements : 4
# Elements : 13 5 45 7
#
# Output:
# 5
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