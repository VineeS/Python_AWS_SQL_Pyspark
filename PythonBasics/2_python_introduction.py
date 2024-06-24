### set a variable 
#1. Slicing

print(3 * 'un' + 'ium')

variable = True
if variable:
    print("In the If Statement")

word = 'Python'
print(word[:4] , word[4:], word[-1], word[-2])

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#    0   1   2   3   4   5   6
#   -6  -5  -4  -3  -2  -1

##2. Strings are immutable in python
word = 'Python'
# word[1]='K'
# print(word)

#### -----> Error TypeError: 'str' object does not support item assignment
##3. We can iterate through string :While strings in Python can be accessed using index notation 
# like arrays in some other languages, they are not exactly arrays in the traditional sense. 
# Strings in Python are sequences of characters, and you can access individual characters using square brackets with index notation,
#  just like with arrays.

my_string = "Python"
print(my_string[0])  # Outputs: P

my_string = "Python"

for char in my_string:
    print(char)


## An object with a fixed value. Immutable objects include numbers, 
    # strings and tuples. Such an object cannot be altered. 
    # A new object has to be created if a different value has to be stored. 
    # They play an important role in places where a constant hash value is needed, for example as a key in a dictionary.


####

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        print("Element to delete : ",user)
        del users[user] 
print("Final users table after deletion : ",users)

new_dic = {}
for u,s in users.items():
    if s == 'active':
        new_dic[u] = s

print(new_dic)

li = ['a','b','c','d','e']
for K, V in enumerate(li):
    print(K,V)


#### *args and **kwargs

def cheeseshop(kind, *arguments, **keywords):
    print("kind 1", kind)
    print("Kind 2", kind)
    print("arguments --->",isinstance(arguments, tuple))

    print("arguments --->",isinstance(arguments, tuple))
    print("keywords --->",isinstance(keywords, dict))

    for arg in arguments:
        print("arguments --> ", arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))

print(f(1))

l = (1,3,2,5)
x = sorted(l, key = lambda x : x)
print(x)

x = lambda m : m+1
print(x(5))

x = lambda a,b : a+b
print(x(2,3))

x = lambda a,b,c:a+b+c+1
print(x(1,2,3))

