from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self):
        return 0

    def authenticate(self):
        return 0

    def withdrawl(self):
        return 0

    def deposit(self):
        return 0

    def displayBalance(self):
        return 0

class SavingAccount(Account):
    def __init__(self):
        self.savingAccounts = {}

    def createAccount(self,name,initialDeposit):
        self.accountNumber = randint(10000,99999)
        self.savingAccounts[self.accountNumber] = [name,initialDeposit]
        print("Account createion has been succesful. Your account number is", self.accountNumber)

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingAccounts.keys():
            if self.savingAccounts[accountNumber][0] == name :
                print('Authenticate Successful')
                self.accountNumber = accountNumber
                return True
            else:
                print('Authenticate Failed')
                return False
        else:
            print("Authenticate Failed")
            return False

    def withdrawl(self, withdrawalAmount):
        if withdrawalAmount > self.savingAccounts[self.accountNumber][1]:
            print("Insufficient balance")
        else:
            self.savingAccounts[self.accountNumber][1] -= withdrawalAmount
            print('Withdrawl was succesful')
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingAccounts[self.accountNumber][1] += depositAmount
        print("Deposit was succesful")
        self.displayBalance()

    def displayBalance(self):
        print('Available balance: ', self.savingAccounts[self.accountNumber][1])

#create object
savingAccount = SavingAccount()
while True:
    try:
        print("Enter 1 to create a new account")
        print("Enter 2 to access an existing account")
        print("Enter 3 to exit")
        userChoice = int(input())
        if userChoice is 1:
            print("Enter your name: ")
            name= input()
            print("Enter the initial deposit: ")
            deposit= int(input())
            savingAccount.createAccount(name,deposit)
        elif userChoice is 2:
            print("Enter your name: ")
            name = input()
            print("Enter your account number: ")
            accountNumber = int(input())
            autheticationStatus = savingAccount.authenticate(name, accountNumber)
            if autheticationStatus is True:
                while True:
                    try:
                        print("Enter 1 to withdraw")
                        print("Enter 2 to deposit")
                        print("Enter 3 to display available balance")
                        print("Enter 4 to go back to the previous menu")
                        userChoice = int(input())
                        if userChoice == 1:
                            print("Enter a withdrawal amount")
                            withdrawalAmount = int(input())
                            savingAccount.withdrawl(withdrawalAmount)
                        elif userChoice == 2:
                            print('Enter an amount to be deposited')
                            depositAmount = int(input())
                            savingAccount.deposit(depositAmount)
                        elif userChoice == 3:
                            savingAccount.displayBalance()
                        elif userChoice == 4:
                            break
                        else:
                            print('Enter valid integer in range 1 to 4')
                    except ValueError:
                        print('-'*43)
                        print("| No valid integer! Please try again ... |")
                        print('-' * 43)
        elif userChoice == 3:
            quit()
        else:
            print('Enter valid integer in range 1 to 3')
    except ValueError:

B
A
A
A
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
B
A
A
A
A
A
A
A
A
A
B
B
B
A
A
A
A
A
A
A
A
A
B
B
B
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
A
B
B
B
B
B
B
B
B
B
        print("No valid integer! Please try again ...")
