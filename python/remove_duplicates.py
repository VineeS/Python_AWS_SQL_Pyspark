def remove_duplicates(string_val):
    dict_for_count = {}
    for i in string_val:
        if i in dict_for_count:
            dict_for_count[i] +=1

        else:
            dict_for_count[i] = 1

    print(dict_for_count)
    without_duplicates = ""
    for key, value in dict_for_count.items():
        
        if value == 1:
            print(key, value)
            without_duplicates += key
    return without_duplicates


string_val = "traveller"
print(remove_duplicates(string_val))
