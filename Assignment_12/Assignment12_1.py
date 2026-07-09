# ----------------------------------------------------------
# 1. Vowel or Consonant Check
# Problem:
# Accept one character and check whether it is a vowel
# or a consonant.
#
# Example:
# Input : a
# Output: Vowel
# ----------------------------------------------------------

def Che_Vowel(cAlpha):

    if (cAlpha == 'a' or cAlpha == 'e' or cAlpha == 'i' or cAlpha == 'o' or cAlpha == 'u'):
        return True
    else:
        return False


def main():

    cRet = 0
    print("Enter the Chatercter ")
    cValue = str(input())

    cRet = Che_Vowel(cValue)

    if(cRet == True):
        print(f"{cValue} Is Vowel ")
    else:
          print(f"{cValue} Is Consonant ")

if __name__ == "__main__":
    main()