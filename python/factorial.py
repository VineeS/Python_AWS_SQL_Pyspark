def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        for i in range(1, number+1):
            fact = fact * i
    return fact 


number = 0
print(factorial(number))

def factorial_one(number_fact):
    if number_fact == 0 or number_fact == 1:
        return 1
    return number_fact * factorial_one(number_fact-1)

print(factorial_one(6))