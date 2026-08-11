# ==========================================================
# 2. Count Words in a File
# ==========================================================

# Problem:
# Write a Python program which accepts a file name from
# the user and counts the total number of words in that file.
#
# Input:
# Demo.txt
#
# Expected Output:
# Total number of words in Demo.txt.
#===========================================================

def main():
    try:

        fobj = open("Marvellous.txt","r")
        print("File Successfully Created")

        Data = fobj.read()

        word = Data.split()

        print("Total number of words in Marvellous.txt.",len(word))

        fobj.close()

    except FileExistsError as eobj:
        print("File Not Found")

if __name__ == "__main__":
    main()