n = int(input())
lst = []
h = 0
for _ in range(n):
    k = int(input())
    h = max(h, k)
    lst.append(k)

res = 0
for i in range(h): #해수면의 높이
    cnt = 0
    for j in range(1, n):
        if lst[j] - i <= 0 and lst[j-1] - i > 0:
            cnt += 1
    if lst[-1] - i > 0:
        cnt += 1
    res = max(res, cnt)
print(res)