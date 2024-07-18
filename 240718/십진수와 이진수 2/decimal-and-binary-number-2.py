n = list(input())

res = 0
for i in range(len(n)):
    res += int(n[i]) * 2 ** (len(n)-i-1)

res *= 17
res = list(bin(res))
print(*res[2:], sep='')