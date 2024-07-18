n = int(input())
lst = [0 for _ in range(2000)]

cur = 1000
for _ in range(n):
    l, d = input().split()
    if d == 'R':
        for i in range(cur, cur + int(l)):
            lst[i] += 1
            cur += 1
    else:
        for i in range(cur-1, cur - int(l) -1, -1):
            lst[i] += 1
            cur -= 1
    #print(cur)

res = 0
for i in range(2000):
    #if lst[i] != 0:
        #print(i, lst[i])
    if lst[i] >= 2:
        res += 1
print(res)