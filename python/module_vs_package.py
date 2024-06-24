#this is module_vs_package.py
def module_desc(name):
    return f"this is my name : {name} !"

#consider this as other.py file
import module_vs_package
message = module_vs_package.module_desc("Alice")
print(message)


class Name:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def fullName(self):
        return f"My full name is {self.name} {self.surname}"
    

# Module:
# Definition:

# A module is a single Python file containing reusable code.
# It typically consists of functions, classes, and variables.
# File Structure:

# A module is a single file with a .py extension.
# Importing:

# You import a module using the import statement.
# Example:
# python
# Copy code
# # example_module.py
# def greet(name):
#     return f"Hello, {name}!"

# # main_script.py
# import example_module
# message = example_module.greet("Alice")
# print(message)
# Package:
# Definition:

# A package is a collection of Python modules organized in a directory hierarchy.
# It must contain a special file named __init__.py.
# File Structure:

# A package is a directory that contains multiple Python files (modules) and the __init__.py file.
# Example:
# markdown
# Copy code
# my_package/
# ├── __init__.py
# ├── module1.py
# └── module2.py
# Importing:

# You import a module from a package using dot notation.
# Example:
# python
# Copy code
# # __init__.py
# # This file can be empty or may contain package-level initialization code.

# # module1.py
# def func1():
#     return "Function 1"

# # module2.py
# def func2():
#     return "Function 2"

# # main_script.py
# from my_package import module1, module2
# result1 = module1.func1()
# result2 = module2.func2()
# print(result1)
# print(result2)
# Key Differences:
# Structure:

# A module is a single file, while a package is a directory containing multiple 
# modules and an __init__.py file.
# Importing:

# Modules are imported using the import statement.
# Modules within a package are imported using dot notation.
# Initialization:

# Modules do not require an initialization file.
# Packages must have an __init__.py file (even if it's empty) to be recognized as a package.
# Organization:

# Modules are typically used for small units of code.
# Packages are used to organize and group related modules, providing a hierarchical structure.
# In summary, modules are individual files containing Python code,
# while packages are collections of modules organized in a directory hierarchy. 
# Packages allow for a more organized and hierarchical structure in larger projects.

