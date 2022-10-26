
class BankAccount:
    branch = "Chase"
    Location = "California" 
    
    def __init__(self, name, int_rate = .03, balance = 0): 
        self.name = name
        self.int_rate = int_rate
        self.balance = balance 

    def deposit(self, amount):
        self.balance = amount + self.balance
        return self 
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
        else: 
            self.balance = self.balance - 35
            print("Insufficient funds: Charging a $35 fee")
        return self    
    
    def display_account_info(self):
        print(f"{self.name}'s account balance is: {self.balance}")
        print("Dang boi, you rich aren't you?")
    
    def yield_interest(self):
        self.balance += self.balance * self.int_rate 
        return self

Emily = BankAccount("Tony",.2, 10000)

Branden_Hagge = BankAccount("Branden",.1,10000)

Branden_Hagge.display_account_info()

Branden_Hagge.deposit(2500).withdraw(10000).deposit(25000).deposit(8000).yield_interest().display_account_info()

Emily.deposit(4500).withdraw(10000).deposit(18000).deposit(8000).withdraw(4000).deposit(3000).yield_interest().display_account_info()
print(BankAccount.branch)
