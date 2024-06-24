class X:
    def __init__(self):
        self.__num1 = 5
        self.num2 = 2

    def display_values(self):
        print(self.__num1, self.num2)
class Y(X):
    def __init__(self):
        super().__init__()
        self.__num1 = 1
        self.num2 = 6 
obj = Y()
obj.display_values()

# In the given code, there is a base class X with a private attribute __num1 and a 
# derived class Y that inherits from X. Both classes have an __init__ method where __num1 
# and num2 are defined with different values. The derived class Y overrides the values of __num1 and num2.

# Here's a step-by-step explanation of why the output is 5 and 6:

# An object obj of class Y is created.
# When obj is instantiated, the __init__ method of class Y is called.
# In the __init__ method of class Y, super().__init__() is called, which invokes the __init__ method 
# of the base class X. This initializes self.__num1 to 5 and self.num2 to 2 in the instance of class Y.
# After calling super().__init__(), the derived class Y initializes its own __num1 to 1 and num2 to 6.
# Now, when obj.display_values() is called, it invokes the display_values method from the base class X. 
# This method prints the values of self.__num1 and self.num2. Since __num1 is private in both the base and derived classes,
#  the one in the derived class Y does not override the one in the base class X.

# Therefore, the output of obj.display_values() is 5 and 6, reflecting the values of self.__num1 and self.num2 as defined in the base class X. 
# The private attribute __num1 is still accessed from the base class, and the overridden values in the derived class do not affect it.

class Person:
   def __init__(self, first_name, last_name):
       self.first_name = first_name
       self.last_name = last_name

first_name = "XYZ"
person = Person(first_name, "ABC")
first_name = "LMN"
print(person.first_name)
person.last_name = "PQR"
print(person.first_name, person.last_name)

# first_name = "XYZ": A variable first_name is defined with the value "XYZ".
# person = Person(first_name, "ABC"): An instance of the Person class is created with first_name set to the value of the variable, which is "XYZ".
# first_name = "LMN": The variable first_name is reassigned the value "LMN".
# print(person.first_name): This prints the first_name attribute of the person object, which was set during the object creation and remains "XYZ".
# person.last_name = "PQR": The last_name attribute of the person object is updated to "PQR".
# print(person.first_name, person.last_name): This prints the first_name and last_name attributes of the person object. The first_name is still "XYZ", and the last_name is now "PQR".

class Parent(object):
    pass
class Child(Parent):
    pass

print(issubclass(Child,Parent))
print(issubclass(Parent, Child))

## also check if the object is instance 
obj1 = Parent()
obj2 = Child()
print(isinstance(obj1, Child))
print(isinstance(obj1, Parent))

#### Constructor in python
class name_class:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print("my name is ",self.name)

obj1 = name_class("Vinee")
obj1.print_name()


### difference between *args Arbitrary Number of Positional Arguments and **kwarg Arbitrary Number of Keyword Arguments
def example_function(arg1, *args, kwarg1="default", **kwargs):
    print(f"arg1: {arg1}")
    print(f"args: {args}")
    print(f"kwarg1: {kwarg1}")
    print(f"kwargs: {kwargs}")

example_function(1, 2, 3, kwarg1="custom", key1="value1", key2="value2")


def example_function(arg1, *args, arg2):
    print(f"arg1: {arg1}")
    print(f"args: {args}")
    print(f"arg2: {arg2}")

   
example_function(1, 2, 3, arg2= 4)


# Key characteristics of Python dictionaries:

# Unordered: The items in a dictionary are not ordered. 
# In Python 3.7 and later, dictionaries maintain the order of insertion, but you should 
# not rely on this behavior in earlier versions or in all scenarios.

# Mutable: You can modify a dictionary by adding, updating, or removing key-value pairs.

# Unique Keys: Each key in a dictionary must be unique. However, values can be duplicated.

# --------- What is PYTHONPATH 

# Example:
# Let's say you have the following directory structure:

# lua
# Copy code
# /project
# |-- main.py
# |-- mymodule
# |   |-- __init__.py
# |   |-- module1.py
# |   |-- module2.py
# And you want to import module1.py from main.py. You can set PYTHONPATH as follows:

# code
# export PYTHONPATH=/path/to/project

# Or in main.py:
# # main.py
# import sys
# sys.path.append("/path/to/project")

# from mymodule import module1

# # Rest of your script...
# By setting the PYTHONPATH to include the project directory, you allow the Python interpreter to find modules within that directory structure.

# Keep in mind that modifying PYTHONPATH affects the entire Python environment. It's often more convenient to use virtual environments or to manage dependencies with tools like pip and requirements.txt to avoid conflicts between projects.

def my_function():
    local_variable = 10
    print("local_variable ",local_variable)

my_function()


def outer_function():
    outer_variable = 10

    def inner_function():
        nonlocal outer_variable
        outer_variable += 1
        print(outer_variable)

    inner_function()

outer_function()
