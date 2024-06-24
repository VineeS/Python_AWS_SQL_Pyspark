def can_reach_end(A):
    furthest_to_reach , last_index = 0, len(A)-1
    i = 0
    while i <= furthest_to_reach and furthest_to_reach < last_index:
        print(furthest_to_reach,  A[i] + 1)
        furthest_to_reach = max(furthest_to_reach , A[i] + i)
        i += 1

    return furthest_to_reach >= last_index

A = [3,3,1,0,2,0,1]
print(can_reach_end(A))