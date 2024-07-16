a, b = map(int, input().split())

if a < b:
    a, b = b, a

res = 0
for i in range(a, b+1):
    if i % 5 == 0:
        res += i

print(res)