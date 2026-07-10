# ----------------------------------------------------------
# 8. Print '*' N Times
# Problem:
# Accept one number and print that many '*'
# characters on the screen.
#
# Example:
# Input : 5
# Output:
# * * * * *
# ----------------------------------------------------------

def Display(No):

    print("Output : ")
    for iCnt in range(1,No+1):
        print("*")


def main():

    print("Enter the Number : ")
    Value = int(input())

    Display(Value)

if __name__ == "__main__":
    main()
