def command_string(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    stack_for_comman = []

    for i in range(max(len_str1, len_str2)):
        if i < len_str1 and str1[i].upper() in str2.upper():
            stack_for_comman.append(str1[i])
        if i < len_str2 and str2[i].upper() in str1.upper():
            stack_for_comman.append(str2[i])

    stack_for_comman = set(stack_for_comman)
    return len(stack_for_comman)

print(command_string("Hell", "helper"))  # Output: 4



