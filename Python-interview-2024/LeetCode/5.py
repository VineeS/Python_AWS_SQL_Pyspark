# def longestPalindrome(s):
#         if len(s) <= 1:
#             return s
        
#         Max_Len=1
#         Max_Str=s[0]
#         for i in range(len(s)-1):
#             for j in range(i+1,len(s)):
#                 print('i',i)
#                 print('j',j)
#                 if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
#                     Max_Len = j-i+1
#                     Max_Str = s[i:j+1]

#         return Max_Str
    
# s = 'babad'
# longestPalindrome(s)


def longestPalindrome(s):
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            print('left ',left)
            print('right ',right)
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            print('Calling odd expand from center, i : ', i)
            odd = expand_from_center(i, i)
            print('odd : ' ,odd)
            print('Calling even expand from center, i  : ', i)
            even = expand_from_center(i, i + 1)
            print('even : ',even)

            if len(odd) > len(max_str):
                print("In odd")
                max_str = odd
            if len(even) > len(max_str):
                print("In even")
                max_str = even

        return max_str

s = 'baabsdalad'
print(longestPalindrome(s))