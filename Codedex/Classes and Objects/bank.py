class BankAccount:
    def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
        

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}€ into account {self.account_id}. New balance: {self.balance}€")
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrew {amount}€ from account {self.account_id}. New balance: {self.balance}€")
        return self.balance

    def display_balance(self):
        print(f"Account {self.account_id} balance: {self.balance}€")
        return self.balance

print("Welcome to the Bank of Python")
account_id = int(input("Enter your account ID: "))
pin = int(input("Enter your PIN: "))


account = BankAccount("Default", "Default", account_id, "Checking", pin, 0) 
#creates an instance of the BankAccount class so we can use the methods of the class


def Answer ():
    option = int(input("Please select an option: \n1. Deposit \n2. Withdraw \n3. Display Balance \n4. Exit \n"))

    if option == 1:
        amount = int(input("Enter the amount to deposit in €: "))
        account.deposit(amount)

    elif option == 2:
        amount = int(input("Enter the amount to withdraw in €: "))
        account.withdraw(amount)

    elif option == 3:
        account.display_balance()

    elif option == 4:
        print("Thank you for using the Bank of Python")
        quit()
    else:
        print("Invalid option. Please try again.")

Answer()

