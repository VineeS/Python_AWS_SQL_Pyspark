class Employee:
    raise_amount = 1.03
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary
        self.email = name+surname+'@email.com'

    def fullname(self):
        return '{} {}'.format(self.name,self.surname)
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amount)
        return self.salary

class Developer(Employee):
    raise_amount = 1.10



class EmployeeDetail(Employee):
    def __init__(self, name, surname, salary, programming_lang):
        super().__init__(name,surname,salary)
        self.programming_lang = programming_lang


class ProjectManager(Employee):
    raise_amount = 1.20
    def __init__(self,name, surname, salary, list_of_emp=None):
        super().__init__(name,surname,salary)
        if list_of_emp is None:
            self.list_of_emp = []
        else:
            self.list_of_emp = list_of_emp

    def add_emp(self,emp):
        if emp not in self.list_of_emp:
            self.list_of_emp.append(emp)

    def remove_emp(self,emp):
        if emp in self.list_of_emp:
            self.list_of_emp.remove(emp)

    def print_emp(self):
        for emp in self.list_of_emp:
            print('-->', emp.fullname())

emp1 = Employee('Vinee', 'Shukla', 80000)
emp2 = Employee('Aman', 'Sharma', 10000)

print(emp1.fullname())

print(emp2.apply_raise())

emp1 = Developer('Vinee', 'Shukla', 80000)
emp2 = Developer('Aman', 'Sharma', 10000)


print(emp1.fullname())
print(emp2.apply_raise())

# print(help(Developer))
emp1 = Employee('Vinee', 'Shukla', 80000)
print("Employee Raise", emp1.apply_raise())

# print(Developer.__mro__) ## output --> (<class '__main__.Developer'>, <class '__main__.Employee'>, <class 'object'>)
print("Developer Raise ",emp1.apply_raise())

emp1 = ProjectManager('Vinee', 'Shukla', 80000)
print("Manager Raise ",emp1.apply_raise())

emp1 = EmployeeDetail('Robo', 'Cop', 990000, 'Python')
print(emp1.fullname())
print(emp1.programming_lang)
print(emp1.email)

emp1 = Employee('Vinee', 'Shukla', 80000)
emp2 = Employee('Aman', 'Sharma', 10000)
emp3 = Employee('Honey', 'Sharma', 20000)
emp4 = Employee('Yash', 'Shukla', 30000)

m1 = ProjectManager('Sue', 'Smith',90000, [emp1, emp2] )
print(m1.email)
print(m1.print_emp())
m1.add_emp(emp3)
m1.add_emp(emp4)
print(m1.print_emp())
m1.remove_emp(emp1)
m1.print_emp()

print('isinstance')
print(isinstance(m1, ProjectManager)) ### True
print(isinstance(m1, Developer)) ### False
print('issubclass')
print(issubclass(Developer, Employee)) ## True
print(issubclass(Developer, ProjectManager)) ## False

