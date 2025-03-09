class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"    
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format (self.first, self.last)
    


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("Test", "User", 60000)


print(emp_1.email)
print(emp_2.email)



print(emp_1.fullname())
print(Employee.fullname(emp_2))


print(emp_1.raise_amount)


print(Employee.num_of_emps)