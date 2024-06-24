def frequencySort(s):
        dict_for_str = {}
        for i in s:
            if i in dict_for_str:
                dict_for_str[i] +=1

            else:
                dict_for_str[i] = 1

        sorted_dict = dict(sorted(dict_for_str.items(), key=lambda item: item[1], reverse=True))
        print(sorted_dict)
        str_sorted = ""
        for key, val in sorted_dict.items():
            str_sorted += (key*val)
        return str_sorted
print(frequencySort("ttrrrree"))