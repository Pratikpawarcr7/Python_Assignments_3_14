# ==========================================================
# 3. Display File Line by Line
# ==========================================================
# Problem:
# Write a Python program which accepts a file name from
# the user and displays the contents of the file line by line
# on the screen.
#
# Input:
# Demo.txt
#
# Expected Output:
# Display each line of Demo.txt one by one.
#==============================================================

def main():
    File = str(input("Enter the File Name : "))

    try:

        fobj = open(File,"r")

        for Line in fobj:
            print(f"Number of Lines in {File} :",Line," ")

        fobj.close()

    except Exception as eobj:
        print("File Not Found")
        

if __name__ == "__main__":
    main()













