# ==========================================================
# 4. Copy File Contents into Another File
# ==========================================================
#===========================================================
# Problem:-
#==========
# Write a Python program which accepts two file names
# from the user.
#
# - First file is an existing file.
# - Second file is a new file.
#
# Copy all contents from the first file into the second file.
#
# Input:
# ABC.txt Demo.txt
#
# Expected Output:
# Contents of ABC.txt copied into Demo.txt.
#===========================================================

def main():

    Source = input("Enter source file name : ")
    Destination = input("Enter destination file name : ")

    try:
        fobj1 = open(Source, "r")
        fobj2 = open(Destination, "w")

        Data = fobj1.read()

        fobj2.write(Data)

        fobj1.close()
        fobj2.close()

        print("File content copied successfully.")

    except Exception as eobj:
        print("Error :", eobj)


if __name__ == "__main__":
    main()







