a, b = map(int, input().split())
s = list(str(a + b))
res = 0
for i in range(len(s)):
    if s[i] == '1':
        res += 1
print(res)