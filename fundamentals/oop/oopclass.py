# declare a class in python

class User:
    def __init__(self,name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self



cedrick =User("Cedrick", "cedrick@gmail.com")
# cedrick.make_deposit(2000)
# cedrick.make_deposit(100)
# cedrick.make_deposit(2300)
# cedrick.make_deposit(2800)
# cedrick.make_deposit(4565)


cedrick.make_deposit(2000).make_deposit(100).make_deposit(2300).make_deposit(2800).make_deposit(4565)

arlette = User("Arlette", "arlette@gmail.com")
arlette.make_deposit(5000)


print(f"{cedrick.name}'s account balance is: {cedrick.account_balance}")
print(f"{arlette.name}'s account balance is: {arlette.account_balance}")
