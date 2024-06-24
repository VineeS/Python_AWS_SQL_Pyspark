def even_odd(A):
    next_even , next_odd = 0,len(A)-1
    while next_even < next_odd:
        print("e - ", next_even, "o - ", next_odd,)
        if A[next_even] % 2 == 0 :
            next_even +=1

        else:
            print("A[next_even]",A[next_even], " A[next_odd]",  A[next_odd])
            A[next_even] , A[next_odd] = A[next_odd], A[next_even]
            print("A[next_even]",A[next_even], " A[next_odd]",  A[next_odd])
            print("A --> ",A)
            next_odd -=1

    return A
A = [1,3,4,5,2]
print(even_odd(A))

#### List comprehension 
L= [1,2,3,4]
B = [x*x for x in L]
print("List Comprehension One ", B)

B = [x for x in L if x%2 == 0]
print("List Comprehension Two ", B)

A = (1,2,3) 
B = ('a','b')
ans  = [(x,y) for x in A for y in B]
print("List Comprehension Three ", ans)

M = [['a','b','c'],['d','e','f']]
new_list = [x for row in M for x in row]
print("List Comprehension Three ", new_list)


M = [[1,2,3],[4,5,6]]
new_list = [[x**2 for x in row] for row in M]
print("List Comprehension Three ", new_list)
