n, m = map(int, input().split())

alst = []
a = 0
for _ in range(n):
    l, d = input().split()
    if d == 'R':
        for i in range(int(l)):
            a += 1
            alst.append(a)
    else:
        for i in range(int(l)):
            a -= 1
            alst.append(a)

blst = []
b = 0
for _ in range(m):
    l, d = input().split()
    if d == 'R':
        for i in range(int(l)):
            b += 1
            blst.append(b)
    else:
        for i in range(int(l)):
            b -= 1
            blst.append(b)

if len(alst) > len(blst):
    for i in range(len(alst) - len(blst)):
        blst.append(blst[-1])

if len(alst) < len(blst):
    for i in range(len(blst) - len(alst)):
        alst.append(alst[-1])

cnt = 0
for i in range(1, len(alst)):
    if alst[i] == blst[i] and alst[i-1] != blst[i-1]:
        cnt += 1

print(cnt)