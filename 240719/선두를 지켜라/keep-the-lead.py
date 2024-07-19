n, m = map(int, input().split())

alst = []
blst = []
a = 0
b = 0 
for _ in range(n):
    va, ta = map(int, input().split())
    for i in range(ta):
        a += va
        alst.append(a)

for _ in range(m):
    vb, tb = map(int, input().split())
    for i in range(tb):
        b += vb
        blst.append(b)

res = []
cnt = 0
if alst[0] > blst[0]:
    res.append(0)
elif alst[0] < blst[0]:
    res.append(1)
else:
    res.append(2)

for i in range(len(alst)):
    if alst[i] > blst[i]:
        if res[-1] == 1:
            cnt += 1
        res.append(0)
    elif alst[i] < blst[i]:
        if res[-1] == 0:
            cnt += 1
        res.append(1)
    else:
        res.append(res[-1])
print(cnt)