# class User:
#     # declaring a class attribute
#     bank_name = "First National Dojo"		
#     def __init__(self):
#         self.name = "Michael"
#         self.email = "michael@codingdojo.com"
#         self.account_balance = 0

# cedrick = User()
# brendaline = User()

# cedrick.bank_name = "BICEC"
# cedrick.email = "cedrick@gmail.com"
# cedrick.dob = "19/2/2000"

# print(cedrick.bank_name)
# print(cedrick.dob)
# print(brendaline.account_balance)


# print(brendaline.bank_name)

class User:
    bank_name = "Afriland First Bank"

    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0

        

newUser =User("Wallace","wallace@gmail.com")

print(newUser.email)
print(newUser.bank_name)