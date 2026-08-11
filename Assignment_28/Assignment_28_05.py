# ==========================================================
# 5. Search a Word in File
# ==========================================================
#
# Problem:
#----------
# Write a Python program which accepts a file name and
# a word from the user and checks whether that word is
# present in the file or not.
#
# Input:
# Demo.txt Marvellous
#
# Expected Output:
# Display whether the word Marvellous is found in Demo.txt
# or not.
#
# ==========================================================

def main():

    FileName = input("Enter file name : ")
    Word = input("Enter word to search : ")

    try:
        fobj = open(FileName, "r")

        Data = fobj.read()

        if Word in Data:
            print("Word found in file")
        else:
            print("Word not found in file")

        fobj.close()

    except Exception as eobj:
        print("Error :", eobj)


if __name__ == "__main__":
    main()