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

        fobj = open("Marvellous.txt","w")
        print("File Successfully Created")

        fobj.write("Marvellous Infosystem\n")
        fobj.write("Marvellous Infosystem Pune")

        fobj.close()

    except FileExistsError as eobj:
        print("File Not Found")

if __name__ == "__main__":
    main()