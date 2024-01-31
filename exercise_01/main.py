#Ryan Breedlove
from BankAccount import BankAccount

#Creates the bank account
account = BankAccount('Azrael Razgriz', 1000)

# Deposit money to the account
account.deposit(500)

#Withdraws money from the account
account.withdraw(200)

#Sets up and prints the balance information
balance_info = account.get_balance()
print(balance_info)