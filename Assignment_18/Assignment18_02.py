# ----------------------------------------------------------
# 2. Maximum Number from List
# Problem:
# Accept N numbers from the user and store them in a List.
# Return the maximum number from that List.
#
# Example:
# Input :
# Number of elements : 7
# Elements : 13 5 45 7 4 56 34
#
# Output:
# 56
# ----------------------------------------------------------

def Max_Element(iLength,Members):

    Sum = 0
    iMax = Members[0]
    for iCnt in range(0,iLength):
        if(iMax < Members[iCnt]):
            iMax = Members[iCnt]
        
        return iMax 

def main():
    Elements = []

    print("How Many Members You Want in Your List : ")
    iValue1 = int(input())

    print("Enter the Elements : ")
    
    for iCnt in range(0,iValue1):
        iValue2 = int(input())
        Elements.append(iValue2)

    print("Your Input List is : ",Elements)

    Ret = Max_Element(iValue1,Elements)

    print("Maximum is : ",Ret)



if __name__ == "__main__":
    main()