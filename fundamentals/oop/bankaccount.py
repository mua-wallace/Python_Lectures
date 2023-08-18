class  BankAccount:
    def __init__(self, int_rate =0.02, balance =0 ):
        self.int_rate = int_rate
        self.balance = balance
       

    def deposit(self, cashin):
        self.balance += cashin
        return self
    
    def withdrawal(self, cashout):
        if self.balance >= cashout:
            self.balance -= cashout
        else:
            self.balance -= 5
            print("Insufficient funds , a charge of 5frs  has been deducted")
        return self
        
    
    def display_account_info(self):
        print(f"Balance: {self.balance}frs")
        return self
    
    def transfer_money(self, recipient, amount):
        # recipient.balance += amount
        recipient.deposit(amount)
        # self.balance -= amount
        self.withdrawal(amount)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance*self.int_rate
        return self


accout1 = BankAccount(balance=10000).yield_interest().display_account_info()

