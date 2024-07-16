n, m = map(int, input().split())

if n > m:
    quot = n // m
else:
    quot = 0

lst = []
rest = n % m
for i in range(20):
    div = rest * 10
    lst.append(div // m)
    rest = div % m

print(quot, end='.')
print(*lst, sep='')