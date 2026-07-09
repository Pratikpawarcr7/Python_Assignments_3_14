# ----------------------------------------------------------
# 10. Length of Name
# Problem:
# Accept a name from the user and display
# the length of that name.
#
# Example:
# Input : Marvellous
# Output: 10
# ----------------------------------------------------------

def Count(No):

    print("Length of String : ",len(No))

def main():
    print("Enter the String : ")
    Value = input()

    Count(Value)


if __name__ == "__main__":
    main()