
class Employee:
    
    num_of_emps = 0
    raise_amt= 1.04 

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = firstname + "." + lastname + "@company.com" 
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def apply_raise(self):
        self.salary = int(self.salary * Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

emp1 = Employee('Adam', 'Smith', 50000)
emp2 = Employee('Paul', 'Samuelson', 100000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)
