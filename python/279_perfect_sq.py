def perfect_square_sum(num):
    perfect_sq_till = num//2
    print(perfect_sq_till)
    list_of_sqare = []
    for i in range(1, perfect_sq_till):
        sq = i * i
        if sq > num:
            break
        else: 
            list_of_sqare.append(sq)
        
    print(list_of_sqare)

perfect_square_sum(12)
