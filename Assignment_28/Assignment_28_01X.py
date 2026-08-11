# ==========================================================
# 1. Count Lines in a File
# ==========================================================

# Problem:
# Write a Python program which accepts a file name from
# the user and counts how many lines are present in the file.
#
# Input:
# Demo.txt
#
# Expected Output:
# Total number of lines in Demo.txt.
#==============================================================

def main():
    try:

        fobj = open("Marvellous.txt","r")
        print("File Successfully Created")

        Data = fobj.readlines()

        print("Total number of lines in Marvellous.txt.",len(Data))

        fobj.close()

    except FileExistsError as eobj:
        print("File Not Found")

if __name__ == "__main__":
    main()