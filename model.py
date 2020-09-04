
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

    @classmethod
    def from_string(cls, emp_str):
        first, last, sal = emp_str.split('-')
        return cls(first, last, sal)
        

emp1 = Employee('Adam', 'Smith', 50000)
emp2 = Employee('Paul', 'Samuelson', 100000)



# Employee.set_raise_amt(1.05)

# print(Employee.raise_amt)
# print(emp1.raise_amt)
# print(emp2.raise_amt)


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'


new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.salary)

