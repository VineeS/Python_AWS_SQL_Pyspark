x = [2,1,5,6]
def bubblesort(x):
    for i in range(0,len(x)-1):
        swap = False
        for j in range(0, len(x)-i-1):
            if x[j] > x[j+1]:
                swap = True
                x[j], x[j + 1] = x[j + 1], x[j]
                

        if not swap:
            break   
    return x
                

print(bubblesort(x))
        



