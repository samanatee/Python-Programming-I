'''
Created on May 6, 2018

@author: Samantha Hangsan
The objective is to use object oriented programming and inheritance in the program.
Create simple bank application that:
    - creates accounts for customers
    - performs simple actions such as deposit, withdraw, and applying annual interest
'''
import random
# Customer class
class Customer:
    def __init__(self, first, last, ssn):
    # initialize customer information
        self.first_name = first
        self.last_name = last
        self.social_security = ssn

    def __str__(self):
    # override __str__ operator to return the customer first name, last name and ssn.
        return '{} {} (SSN: {})'.format(self.first_name, self.last_name, self.social_security)

# BankAccount base class
class BankAccount:
    # initialize account information
    def __init__(self, customer):
        self.customer_info = customer
        self.account_number = "%010d" %random.randrange(1, 10**10)        # For each bank account, a 10 digit random account number must be created.
        self.balance = 0
        self.interest = 0
        self.check_withdrawal = True

    # A bank account can be opened with any amount of initial deposit
    def deposit(self, deposit):
        self.amount_deposited = deposit
        self.balance += self.amount_deposited

    def withdraw(self, withdraw):
        # Amount withdrawn cannot exceed balance.
            # If it does, amount should not be withdrawn and insufficient funds should be reported.
        self.amount_withdrawn = withdraw
        if self.amount_withdrawn <= self.balance:
            self.balance -= self.amount_withdrawn
        else:
            print('{}, Insufficent funds to withdraw ${:0.2f}'.format(self.customer_info, self.amount_withdrawn))

    def applyAnnualInterest(self):
            self.balance += (self.balance * self.interest)

    # Must override __str__ operator to return a pretty string representation of a bank account.
    def __str__(self):
            return '{}, Account Number: {}, Balance: ${:0.2f}'.format(self.customer_info, self.account_number, self.balance)

# Subclasses: Checking Account and Saving Account. These subclasses inherit from the BankAccount base class.
class SavingAccount(BankAccount):
# Saving account accrues 5% fixed interest
    def __init__(self, customer):
        BankAccount.__init__(self, customer)
        self.interest = 0.05
    def applyAnnualInterest(self):
        self.balance += (self.balance * self.interest)

class CheckingAccount(BankAccount):
# Checking account accrues 2% for any amount in excess of $10000
    #(For example, if there is $11000 in the checking account, the interest is only applied to $1000).
    def __init__(self, customer):
        BankAccount.__init__(self, customer)
        self.interest = 0.02
    def applyAnnualInterest(self):
        if self.balance > 10000:
            self.balance += (self.balance - 10000) * self.interest
        else:
            self.balance += (self.balance * self.interest)

def main():
    alin = Customer('Alin', 'Smith', '111-11-1111')
    mary = Customer('Mary', 'Lee', '222-22-2222')

    alinAccnt = CheckingAccount(alin)
    maryAccnt = SavingAccount(mary)

    alinAccnt.deposit(20000)
    print(alinAccnt)
    alinAccnt.withdraw(5000)
    print(alinAccnt)
    alinAccnt.applyAnnualInterest()
    print(alinAccnt)


    maryAccnt.deposit(10000)
    print(maryAccnt)
    maryAccnt.withdraw(15000)
    print(maryAccnt)
    maryAccnt.applyAnnualInterest()
    print(maryAccnt)

if __name__ == '__main__':
    main()