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
        recipient.balance += amount
        # recipient.deposit(amount)
        self.balance -= amount
        # self.withdrawal(amount)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + self.balance*self.int_rate
        return self
    


# User class
class  User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self
        
    
    def display_user_info(self):
        self.account.display_account_info()
        return self
    
    def transfer_money(self, other_user, amount):
        self.account.transfer_money(other_user, amount)
        return self
    
    def yield_interest(self):
        self.account.yield_interest()
        return self


martin = User("Martin","martin@user.com")
brandaline = User("Brendaline","brendaline@user.com")

brandaline.make_deposit(5000).make_deposit(4750).transfer_money("martin",200).display_user_info()

martin.display_user_info()

