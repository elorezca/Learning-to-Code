
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Error, insufficient funds")
        else:
            self.balance -= amount
        return amount
    
    
emmanuel_account = BankAccount("Emmanuel", 1000)

print("Starting balance:", emmanuel_account.balance)
    
emmanuel_account.deposit(2000)

print("Deposited: 2000")

print("New balance:", emmanuel_account.balance)
    
emmanuel_account.withdraw(1000)
    
print("Final balance", emmanuel_account.balance)
        
        