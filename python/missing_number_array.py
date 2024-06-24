def missing_number(list_of_number):
    for i in range(0,len(list_of_number)):
        if list_of_number[i] - list_of_number[i-1] > 1:
            missing_number = list_of_number[i-1]+1
            print(f"missing number is {missing_number}")
            return missing_number
        else:
            pass
    print("No value missing")


list_of_number = [0,1,2,3,4,5]
missing_number(list_of_number)