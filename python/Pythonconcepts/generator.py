def square_of_each_number(nums):
    for i in nums:
        yield (i*i)
    
m = square_of_each_number([1,2,3,4])
print(next(m))
print(next(m))
print(next(m))
print(next(m))



