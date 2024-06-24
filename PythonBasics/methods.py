### Class methods, methods and static methods

## class method
import datetime
class MyClass:
    raise_amount = 1.05
    def __init__(self,name,surname,salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def regular_method(self):
        return 'In Regular Method , my name is {} {} and my salary is {}'.format(self.name, self.surname, self.salary)
    
    
    @classmethod
    def class_method_ex(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod
    def static_method(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp1 = MyClass('Vinee', 'Shukla', 150)
emp2 = MyClass('Aman', 'Sharma', 200)

print(MyClass.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

### class method 
MyClass.class_method_ex(1.06)
print(MyClass.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

### class methods via instances emp1 and emp2
emp1.class_method_ex(1.08)
print(MyClass.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

### class methods as alternative constructors 
emp_str1 = 'John-Doe-70000'
emp_str2 = 'Sean-Doe-90000'
emp_str1 = 'Jame-Doe-50000'

val1=MyClass.from_string(emp_str1)
print(val1.name)
print(val1.surname)
print(val1.salary)

val2=MyClass.from_string(emp_str2)
print(val2.name)
print(val2.surname)
print(val2.salary)

### access regular
print(emp1.regular_method())
print(emp2.regular_method())

### static method
my_date = datetime.date(2016,7,11)
print(MyClass.static_method(my_date))

