import functools
import string

def int_to_str(x):
    is_negative = False
    if x < 0:
        x = -x
        is_negative = True

    s = []
    while True:
        print(f"{ord('0')} + x -> {x} --> {x % 10} = {chr(ord('0') + x % 10)}")
        s.append(chr(ord('0') + x%10))
        x //= 10
        if x == 0:
            break
    print(s)
    return ('-' if is_negative else '') + ''.join(reversed(s))

x = 314
print(type(x))
print(int_to_str(x))
print(type(int_to_str(x)))



import string

def string_to_int(x):
    running_sum = 0
    is_negative = False
    
    # Remove leading and trailing whitespaces
    s = x.strip()
    
    # Check if the number is negative
    if s[0] == '-':
        is_negative = True
        s = s[1:]  # Remove the negative sign
    
    print("Intermediate results:")
    for c in s:
        print(f"running_sum * 10 + string.digits.index('{c}') = {running_sum} * 10 + {string.digits.index(c)}")
        running_sum = running_sum * 10 + string.digits.index(c)
        print(f"running_sum = {running_sum}")

    # If the number was negative, negate the result
    if is_negative:
        running_sum = -running_sum

    print("\nFinal result:")
    return running_sum

# Example usage:
print(string_to_int("123"))    # Output: 123
print(string_to_int("-456"))   # Output: -456

# Explanation of the output:

# For the input string "123", 
# the lambda function first takes running_sum as 0 and c as '1'. 
# It computes 0 * 10 + string.digits.index('1'), which is 0 * 10 + 1, resulting in 1.
# In the next iteration, running_sum becomes 1 and c becomes '2'. 
# It computes 1 * 10 + string.digits.index('2'), which is 10 + 2, resulting in 12.
# In the final iteration, running_sum becomes 12 and c becomes '3'. 
# It computes 12 * 10 + string.digits.index('3'), which is 120 + 3, resulting in 123.
# The final result (123) is returned as the output.

x  = [1,2,3]
val = functools.reduce(lambda a,b: a+b,x,0 )
print(val)