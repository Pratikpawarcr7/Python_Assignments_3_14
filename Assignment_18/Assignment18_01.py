# ----------------------------------------------------------
# 1. Addition of All Elements from List
# Problem:
# Accept N numbers from the user and store them in a List.
# Return the addition of all elements from that List.
#
# Example:
# Input :
# Number of elements : 6
# Elements : 13 5 45 7 4 56
#
# Output:
# 130
#
# Explanation:
# 13 + 5 + 45 + 7 + 4 + 56 = 130
# ----------------------------------------------------------

def Element_Addition(iLength,Members):

    Sum = 0
    for iCnt in range(0,iLength):
        Sum = Sum + Members[iCnt]

    return Sum

def main():
    Elements = []

    print("How Many Members You Want in Your List : ")
    iValue1 = int(input())

    print("How Many Members You Want in Your List : ")
    
    for iCnt in range(0,iValue1):
        iValue2 = int(input())
        Elements.append(iValue2)

    print("Your Input List is : ",Elements)

    Ret = Element_Addition(iValue1,Elements)

    print("Addition is : ",Ret)



if __name__ == "__main__":
    main()