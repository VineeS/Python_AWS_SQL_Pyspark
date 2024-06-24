class MynewClass:
    raise_amount = 1.05
    def __init__(self,salary):
        self.salary = salary
    
    def raise_sal(self):
        self.salary = int(self.salary * MynewClass.raise_amount)


emp1 = MynewClass(500000)
emp2 = MynewClass(600000)



print("emp dict",emp1.__dict__) ## output --> {'salary': 525000}
print("class dict",MynewClass.__dict__) ## output --> {'raise_amount': 1.05,....}
print("--------------------------------------------")
print(emp1.raise_amount)
print(emp2.raise_amount)

print("after change to 1.06")
emp1.raise_amount = 1.33
print(emp1.raise_amount)
print(emp2.raise_amount)
print(emp1.__dict__)
print(emp2.__dict__)
### output 1.05
# 1.05
# 1.05
# 1.05
# 1.05
# 1.05
# no change as we used MynewClass.raise_amount 