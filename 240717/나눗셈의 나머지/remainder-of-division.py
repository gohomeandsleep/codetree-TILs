n, m = map(int, input().split())

res = []
freq = []
while n // m != 0:
    if n % m not in res:
        res.append(n%m)
        freq.append(1)
    else:
        tmp = res.index(n % m)
        freq[tmp] += 1
    n //= m

if n % m not in res:
    res.append(n%m)
    freq.append(1)
else:
    tmp = res.index(n % m)
    freq[tmp] += 1

q = 0
for i in range(len(freq)):
    q += freq[i] ** 2

print(q)