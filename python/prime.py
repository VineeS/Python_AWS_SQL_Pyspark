def prime(number):
    if number <= 1:
        return False
    if number ==2:
        return True

    for i in range(2,int(number*0.5+1)):

        if number % i == 0:
            return False
        else:
            return True   


print(prime(number)) 