n = int(input())
lst = list(map(int, input().split()))
odd = 0
even = 0
for i in range(n):
    if lst[i] % 2 == 0: even += 1
    else: odd += 1

res = 0
while odd >= 1 and even >= 1:
    res += 2
    odd -= 1
    even -= 1

if odd == 0:
    print(res + 1)
else:
    while odd > 0:
        if odd == 1:
            res -= 1
            odd = 0
        elif odd == 2:
            res += 1
            odd = 0
        elif odd == 3:
            res += 2
            odd = 0
        elif odd == 4:
            res += 1
            odd = 0
        else:
            odd -= 3
            res += 1
print(res)