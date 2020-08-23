
class Employee:
    
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = firstname + "." + lastname + "@company.com" 



emp1 = Employee('Adam', 'Smith', 50000)
emp2 = Employee('Paul', 'Samuelson', 100000)

print(emp1.email)

print(emp2.email)

print(' {} {} '.format(emp1.firstname, emp1.lastname))

