# string_val = "hello"
# print(string_val[::-1])

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self,val):
#         self.items.append(val)

#     def pop(self):
#         if not self.is_empty():
#             return self.items.pop()
#         else:
#             return None
    
#     def is_empty(self):
#         return len(self.items) == 0
    
# def revese_string(input):
#     stack = Stack()
#     for char in input:
#         stack.push(char)

#     reversed_string = ''
#     while not stack.is_empty():
#         reversed_string = reversed_string+ stack.pop()
#     return reversed_string

# input = 'viman'
# print(revese_string(input))

def reverse_string(string_val):
    stack_creation = []
    reversed_string = ''
    for i in string_val:
        stack_creation.append(i)


    while stack_creation:
        reversed_string += stack_creation.pop()
    return reversed_string
        

string_val = "Mind"
print(reverse_string(string_val))

