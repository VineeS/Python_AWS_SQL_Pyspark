def count_number(string_for_test, val):
    dic_val = {}
    for i in string_for_test:
        if i in dic_val:
            dic_val[i] +=1

        else:
            dic_val[i] = 1

    for key, value in dic_val.items():
        if key == val:
            return dic_val[key]

string_for_test = "tempert"
val = "t"
print(count_number(string_for_test,val))

