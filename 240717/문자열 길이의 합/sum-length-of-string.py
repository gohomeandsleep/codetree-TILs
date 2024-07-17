T = int(input())

res = 0
cnt = 0
for _ in range(T):
    lst = list(input())
    res += len(lst)
    if lst[0] == 'a':
        cnt += 1

print(res, cnt)