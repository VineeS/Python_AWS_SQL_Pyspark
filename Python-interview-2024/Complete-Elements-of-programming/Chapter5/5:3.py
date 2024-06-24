def mutli(A,B):
    sign = -1 if (A[0] < 0) ^ (B[0] < 0) else 1
    A[0], B[0] = abs(A[0]), abs(B[0])
    result = [0] * (len(A) + len(B))
    for i in reversed(range(len(A))):
        for j in reversed(range(len(B))):
            # print(i,j)
            # print('A[i],B[j]',A[i],B[j])
            print(result)
            
            result[i + j+ 1] += A[i] * B[j]
            # print("result[i + j+ 1] += A[i] * A[j] ---> ",result[i + j+ 1] , A[i] * A[j])

            result[i+j] += result[i+j+1]//10
            # print("result[i+j] += result[i+j+1]//10 --> ",result[i+j] , result[i+j+1]//10)
            result[i+j+1] %= 10
            # print("result[i+j+1] %= 10 --> ",result[i+j+1] , 10)

        # remove the leading zeros
    result = result[next((i for i , x in enumerate(result)
                             if x != 0), len(result)):] or [0]

    return [sign * result[0]] + result[1:]

A = [-1,2,3]
B = [9,8,7]
print(mutli(A,B))

### in this case we get a leading 0 --> [0,2,3,0,0,0]
A = [-1,0,0,0]
B = [2,3]
print(mutli(A,B))