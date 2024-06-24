def palindrome(string_to_validate):
    pal_dict = {}
    for i in string_to_validate:
        if i in  pal_dict:
            pal_dict[i] += 1
        else:
            pal_dict[i] = 1
    print(pal_dict)

    count_odd = 0
    for key, val in pal_dict.items():
    # For a palindrome, at most one character should have an odd count
        if val % 2 != 0:
            count_odd +=1
    return count_odd <=1

test_string = "A man a Plan a canal panama"
if palindrome(test_string.lower()):
    print(f"{test_string} is a palindrome.")
else:
    print(f"{test_string} is not a palindrome.")

test_string = "Rar"
if palindrome(test_string.lower()):
    print(f"{test_string} is a palindrome.")
else:
    print(f"{test_string} is not a palindrome.")
        


def pal(string_to_validate):
    dic = {}
    for i in string_to_validate:
        if i in dic:
            dic[i] +=1

        else:
            dic[i] = 1

    odd_count = 0
    for key, value in dic.items():
        if value % 2 !=0:
            odd_count +=1

    return odd_count <=1



        