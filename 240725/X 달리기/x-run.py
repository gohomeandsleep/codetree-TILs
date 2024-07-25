n = int(input())

k = int(n ** 0.5)
max_m = k ** 2
cnt = 2 * k - 1
rest = n - max_m
#print(cnt, rest, k)
while rest > 0:
    if rest <= k:
        cnt += 1
        break
    else:
        rest -= k
        cnt += 1
print(cnt)