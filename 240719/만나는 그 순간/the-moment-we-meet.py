n, m = map(int, input().split())

alst = []
blst = []
apri = 0
bpri = 0

for i in range(n):
    d, l = input().split()
    if d == 'R':
        for i in range(apri, apri + int(l)):
            alst.append(i)
        apri += int(l)
    else:
        for i in range(apri, apri - int(l), -1):
            alst.append(i)
        apri -= int(l)

for i in range(m):
    d, l = input().split()
    if d == 'R':
        for i in range(bpri, bpri + int(l)):
            blst.append(i)
        bpri += int(l)
    else:
        for i in range(bpri, bpri - int(l), -1):
            blst.append(i)
        bpri -= int(l)

stat = False
for i in range(1, len(alst)):
    if alst[i] == blst[i]:
        stat = True
        print(i)
        break
if stat == False:
    print(-1)