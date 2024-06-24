def palindrome(s):
    for i in range(len(s)//2):
        print(f"Comparing prosition {i} -- {s[i]} and {~i} -- {s[~i]}")
        if s[i] != s[~i]:
            return False
    return True


print(palindrome("vav"))
print(palindrome("value"))
print(palindrome("rotavator"))

K = "rotavator"
t = "aty"
print(K[1])
print(len(K))
print(K + t)
print(K[2:3])
print(K in t)
print(K.strip())
print(K.startswith("l"))
print(K.endswith("l"))
print("Hello, world. This is , Vinee".split(","))
print(3 * '01')
print(' ,'.join(("Guess", "Prince of Maths", "1777-1855")))
print(K.lower())









