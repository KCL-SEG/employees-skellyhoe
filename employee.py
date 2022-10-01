class Employee:
    def __init__(self, name, commission = "", contracts =""):
        self.name = name
        self.commission = commission
        self.contracts = contracts



class EmployeeHourlyWage(Employee):
    def __init__(self, name, wage, hrs, commission="", contracts=""):
        super().__init__(name, commission, contracts)
        self.wage = wage
        self.hrs = hrs

    def get_pay(self):
        if self.commission and self.contracts:
            return self.wage * self.hrs + self.commission * self.contracts
        elif self.commission:
            return self.wage * self.hrs + self.commission
        return self.wage * self.hrs

    def __str__(self):
        if self.commission and self.contracts:
            return self.name + f" works on a contract of {self.hrs} hours at {self.wage}/hour and receives a commission for {self.contracts} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}."
        elif self.commission:
            return self.name + f" works on a contract of {self.hrs} hours at {self.wage}/hour and receives a bonus commission of {self.commission}.  Their total pay is {self.get_pay()}."
        return self.name + f" works on a contract of {self.hrs} hours at {self.wage}/hour.  Their total pay is {self.get_pay()}."


class EmployeeMonthlySalary(Employee):
    def __init__(self, name, salary, commission="", contracts=""):
        super().__init__(name, commission, contracts)
        self.salary = salary

    def get_pay(self):
        if self.commission and self.contracts:
            return self.salary + self.commission * self.contracts
        elif self.commission:
            return self.salary + self.commission
        return self.salary

    def __str__(self):
        if self.commission and self.contracts:
            return self.name + f" works on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.commission}/contract.  Their total pay is {self.get_pay()}."
        elif self.commission:
            return self.name + f" works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission}.  Their total pay is {self.get_pay()}."
        return self.name + f" works on a monthly salary of {self.salary}.  Their total pay is {self.get_pay()}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = EmployeeMonthlySalary('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = EmployeeHourlyWage('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = EmployeeMonthlySalary('Renee', 3000, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = EmployeeHourlyWage('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = EmployeeMonthlySalary('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = EmployeeHourlyWage('Ariel', 30, 120, 600)

# print(f"{billie}\n{charlie}\n{renee}\n{jan}\n{robbie}\n{ariel}")
