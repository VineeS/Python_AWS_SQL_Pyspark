# def dutch_flag_problem(pivot_index, A):
#     pivot = A[pivot_index]
#     print("A[i]","A[j]")
#     for i in range(0,len(A)-1):
#         for j in range(i+1,len(A)):
#             print("In 1st")

#             print(A[i],"  ",A[j])
#             # First Scenario when pivot is small
#             if A[j] < pivot:
                
#                 A[i],A[j] = A[j],A[i]
#                 print("A ---> ",A)
#                 break

#     for i in reversed(range(len(A)-1)):
#         print("i",i)
#         if A[i] < pivot:
#             break
#         for j in reversed(range(i)):
#             print("j ",j)
#             print("In 2nd")

#             print(A[i],"  ",A[j])
#             if A[j] > pivot:
#                 A[i], A[j] = A[j], A[i]
#                 print("A ---> ",A)
#                 break
#     return A




# pivot_index = 2
# A = [4, 6,4,9, 5]
# print(A[pivot_index])

# print(dutch_flag_problem(pivot_index, A))

# #  0,1, 2, 3,4,5,6
# # [0,1, 2, 0,2,1,1]
# #  p = 2


def dutch_flag_problem(pivot_index, A):
    pivot = A[pivot_index]
    smaller , equal, large = 0,0,len(A)
    while equal < large:
        if A[equal] < pivot:
            A[smaller], A[equal] = A[equal], A[smaller]
            smaller , equal = smaller+1, equal+1
            print("A[equal] < pivot",A)
        elif A[equal] == pivot:
            equal +=1
            print("A[equal] = pivot",A)
        else:
            large -=1
            A[equal], A[large] = A[large], A[equal]
            print(equal,large)
            print("A[equal] > pivot",A)

    return A

pivot_index = 3
A = [-3,0,-1,1,1,3,2,1,4,2]
dutch_flag_problem(pivot_index, A)