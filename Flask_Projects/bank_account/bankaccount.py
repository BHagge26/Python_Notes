class BankAccount:
    branch = "Chase"

    def __init__(self, name, int_rate = .05, balance = 0, routing = 32227627): 
        self.balance = balance
        self.int_rate = int_rate
        self.routing = routing
        self.name = name
    def deposit(self, amount):
        self.balance = amount + self.balance
        return self
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance = self.balance - amount
        else:
            self.balance = self.balance - 5
            print("Insufficient funds: Charging a $5 fee")
        return self
    
    def display_account_info(self):
        print(f"{self.name}'s Account balance: {self.balance} Routing Number: {self.routing}")
        return self
    
    def yield_interest(self):
        self.balance += self.balance * self.int_rate 
        return self






Tony = BankAccount("Tony",.2, 10000)

Branden_Hagge = BankAccount("Branden",.1,10000)

Branden_Hagge.display_account_info()

Branden_Hagge.deposit(2500).withdraw(10000).deposit(25000).deposit(8000).yield_interest().display_account_info()

Tony.deposit(4500).withdraw(10000).deposit(18000).deposit(8000).withdraw(4000).deposit(3000).yield_interest().display_account_info()
print(BankAccount.branch)

