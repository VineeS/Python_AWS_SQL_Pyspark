def febo(num):
    stack = []
    stack.append(0)
    stack.append(1)
    for i in range(1,num):
        number = stack[i-1]+stack[i]
        print(number)
        if number < 22:
            stack.append(number)
        else:
            break
    return stack

num = 22
print(febo(num))

