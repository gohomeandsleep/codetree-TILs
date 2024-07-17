a, b = input().split()
a = list(a)
b = list(b)

def extract_numeric_prefix(s):
    for i in range(len(s)):
        if not ('0' <= s[i] <= '9'):
            return s[:i]
    return s

a = extract_numeric_prefix(a)
b = extract_numeric_prefix(b)

a = "".join(a)
b = "".join(b)
print(int(a) + int(b))