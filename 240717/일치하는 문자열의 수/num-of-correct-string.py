n, lst = input().split()
res = 0
for _ in range(int(n)):
    k = input()
    if lst == k:
        res += 1

print(res)