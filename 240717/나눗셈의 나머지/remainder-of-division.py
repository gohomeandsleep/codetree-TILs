n, m = map(int, input().split())

res = []
freq = []
while True:
    #print(n, m)
    if n <= 1:
        break
    if n % m not in res:
        res.append(n%m)
        freq.append(1)
    else:
        tmp = res.index(n % m)
        freq[tmp] += 1
    n //= m

q = 0
for i in range(len(freq)):
    q += freq[i] ** 2

print(q)