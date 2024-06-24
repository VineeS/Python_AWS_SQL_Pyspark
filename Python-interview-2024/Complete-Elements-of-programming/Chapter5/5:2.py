## arbitary precision-interger 

def plus_one(A):
    ### Add 1 to the last digit
    A[-1] += 1
    for i in reversed(range(1,len(A))):
        if A[i] != 10:
            break
        else:
            A[i] = 0
            A[i-1] +=1

    if A[0] == 10:
        A[0] = 1
        A.append(0)

    return A

A = [9,9]
print(plus_one(A))

A = [1,3,9]
print(plus_one(A))

A = [9,9,9]
print(plus_one(A))