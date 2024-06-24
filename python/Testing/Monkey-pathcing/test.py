import A

def cube(self,num):
    return f'cube of a num : {num**3}'

print("cube :",id(cube))
print("square : ",id(A.Power.square))
### monkey patching
A.Power.square = cube
print("after assigning it to the A.Power.square = cube",id(cube))
print("square : ",id(A.Power.square))
obj = A.Power()
print(obj.square(3))

# cube : 4505111584
# square :  4505638912
# after assigning it to the A.Power.square = cube 4505111584
# square :  4505111584
# cube of a num : 27


