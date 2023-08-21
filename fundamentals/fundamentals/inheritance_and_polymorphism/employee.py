class Employee:
    pay_rate = 1.04

    def __init__(self, first_name: str, last_name:str, pay:float) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email =self.generate_email()

    def generate_email(self):
        print(f"{self.first_name.lower()}{self.last_name.lower()}@gmail.com")
        return self
    
    def full_name(self):
        print(f"{self.first_name} {self.last_name}")
        return self
    



class Developer(Employee):
   
    def __init__(self, first_name: str, last_name: str, pay: float, prog_languages:list ) -> None:
        super().__init__(first_name, last_name, pay)
        # Employee().__init__(first_name, last_name, pay)
        self.prog_languages = prog_languages
    def salary(self):
        pass


class Remotedev(Developer):
    def __init__(self, first_name: str, last_name: str, pay: float, prog_languages: list, ) -> None:
        super().__init__(first_name, last_name, pay, prog_languages)
    






employee1 = Employee("Peace", "Kalu", 90000)

dev1 = Developer('Arlette', 'Tatkeu', 500000, ["Javscript","Python"])

print(dev1.prog_languages)




