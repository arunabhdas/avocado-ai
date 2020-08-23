
class Employee:
    
    raise_amount = 1.04 

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = firstname + "." + lastname + "@company.com" 


    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    def apply_raise(self):
        self.salary = int(self.salary * Employee.raise_amount)

emp1 = Employee('Adam', 'Smith', 50000)
emp2 = Employee('Paul', 'Samuelson', 100000)

print(emp1.email)

print(emp2.email)

print(emp1.fullname())
print(emp1.salary)

emp1.apply_raise()

print(emp1.salary)

