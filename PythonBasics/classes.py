class Employee:
    ### constructor 
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last + '@gmail.com'

    ### 
    def print_data(self):
        print('My name is {}{} , pay is {} and email is {}'.format(self.first, self.last, self.pay, self.email))

emp1 = Employee('vinee','shukla',100000)
emp2 = Employee('sharma', 'vinee', 200000)

emp1.print_data()
print(emp1.email)

emp2.print_data()
print(emp2.email)


Employee.print_data(emp1)
### you cannot 
# Employee.email(emp1)



# ```python
# class MyClass:
# ```
# - This line defines a new class named `MyClass`.

# ```python
#     def __init__(self, x):
# ```
# - This line defines a special method called `__init__`, which is the constructor method in Python. 
# It is called when a new instance of the class is created. The `self` parameter refers to the instance itself,
#  and `x` is a parameter passed to initialize the instance.

# ```python
#         self.x = x
# ```
# - This line assigns the value of the parameter `x` to the attribute `x` of the instance (`self`). 
# It initializes an attribute of the instance with the value passed during object creation.

# ```python
#     def print_x(self):
# ```
# - This line defines a method named `print_x` within the `MyClass` class. The `self`
#  parameter refers to the instance on which the method is called.

# ```python
#         print(self.x)
# ```
# - This line prints the value of the attribute `x` of the instance (`self`). 
# It accesses the value of `x` associated with the instance on which the method is called.

# ```python
# # Creating an instance of MyClass
# obj = MyClass(5)
# ```
# - This line creates a new instance of the `MyClass` class, with the argument `5` passed to the 
# constructor (`__init__`). This initializes the `x` attribute of the instance with the value `5`.

# ```python
# # Calling the print_x method on the instance
# obj.print_x()
# ```
# - This line calls the `print_x` method on the instance `obj` of the `MyClass` class. 
#     It prints the value of the `x` attribute associated with the instance `obj`.


#### Class Variable 



class MynewClass:
    raise_amount = 1.22
    def __init__(self,salary):
        self.salary = salary
    
    def raise_sal(self):
        # self.salary = int(self.salary * self.raise_amount) -- you can call using self or MynewClass
        self.salary = int(self.salary * self.raise_amount)
    
emp1 = MynewClass(500000)
emp2 = MynewClass(600000)
print("With self.raise_amount  --------------------")
print(MynewClass.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(emp1.__dict__)
print(emp2.__dict__)

print("after change to 1.06")

emp1.raise_amount = 1.78
print(MynewClass.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(emp1.__dict__)
print(emp2.__dict__)