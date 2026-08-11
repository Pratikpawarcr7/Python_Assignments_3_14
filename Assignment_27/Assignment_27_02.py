# ==========================================================
# 2. BankAccount Class
# ==========================================================

# Problem:
# Write a Python program to implement a class named
# BankAccount with the following requirements:
#
# 1. The class should contain two instance variables:
#
#    Name
#    - Stores the account holder name.
#
#    Amount
#    - Stores the account balance.
#
# 2. The class should contain one class variable:
#
#    ROI
#    - Rate of Interest.
#    - Initialize ROI to 10.5.
#
# 3. Define a constructor __init__() that accepts Name and
#    initial Amount.
#
# 4. Implement the following instance methods:
#
#    Display()
#    - Displays the account holder name and current balance.
#
#    Deposit()
#    - Accepts an amount from the user and adds it to
#      the account balance.
#
#    Withdraw()
#    - Accepts an amount from the user and subtracts it
#      from the account balance.
#    - Withdrawal should be allowed only if sufficient
#      balance is available.
#
#    CalculateInterest()
#    - Calculates and returns the interest using the formula:
#
#      Interest = (Amount * ROI) / 100
#
# 5. Create multiple objects of the BankAccount class and
#    demonstrate all the methods.
#
# ==========================================================

# ==========================================================
# 2. BankAccount Class
# ==========================================================

class BankAccount:


    ROI = 10.5

    
    def __init__(self, Name, Amount):

        
        self.Name = Name
        self.Amount = Amount

    
    def Display(self):

        print("Account Holder Name :", self.Name)
        print("Current Balance     :", self.Amount)

    
    def Deposit(self):

        Value = float(input("Enter amount to deposit : "))

        self.Amount = self.Amount + Value

        print("Amount deposited successfully.")

    
    def Withdraw(self):

        Value = float(input("Enter amount to withdraw : "))

        
        if Value <= self.Amount:

            self.Amount = self.Amount - Value

            print("Amount withdrawn successfully.")

        else:

            print("Insufficient balance.")

    
    def CalculateInterest(self):

        Interest = (self.Amount * BankAccount.ROI) / 100

        return Interest


def main():

    Obj1 = BankAccount("Pratik", 10000)

    Obj1.Display()

    Obj1.Deposit()

    Obj1.Display()

    Obj1.Withdraw()

    Obj1.Display()

    print("Interest :", Obj1.CalculateInterest())


    Obj2 = BankAccount("Rahul", 20000)

    Obj2.Display()

    Obj2.Deposit()

    Obj2.Display()

    Obj2.Withdraw()

    Obj2.Display()

    print("Interest :", Obj2.CalculateInterest())

if __name__ == "__main__":
    main()