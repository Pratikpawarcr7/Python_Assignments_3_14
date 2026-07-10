# ----------------------------------------------------------
# 7. Lambda Function using filter()
# Problem:
# Accept a list of strings and return a list of strings
# whose length is greater than 5.
#
# Example:
# Input : ["Python", "C", "Java", "Programming"]
# Output: ["Python", "Programming"]
# ----------------------------------------------------------

Str_Length = lambda No : len(No) > 5
def main():

    Word = list()

    print("How many String You Want In your List : ")
    Value = int(input())

    print("Enter the Strings : ")
    for iCnt in range(Value):
        cName = input()
        Word.append(cName)

    print("Your Input List Before Filter : ",Word)

    F_Data = list(filter(Str_Length,Word))
    print("Your Input List After Filter : ",F_Data)

if __name__ == "__main__":
    main()
