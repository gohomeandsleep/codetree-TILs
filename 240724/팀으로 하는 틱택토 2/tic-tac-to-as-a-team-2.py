lst = []
for _ in range(3):
    p = list(str(input()))
    for i in range(3):
        p[i] = int(p[i])
    lst.append(p)
cnt = 0

for i in range(3):
    tmp = [lst[i][0], lst[i][1], lst[i][2]]
    if tmp[0] == tmp[1] and tmp[1] == tmp[2]:
        cnt += 0
    elif tmp[0] != tmp[1] and tmp[1] != tmp[2] and tmp[0] != tmp[2]:
        cnt += 0
    else:
        cnt += 1

for i in range(3):
    tmp = [lst[0][i], lst[1][i], lst[2][i]]
    if tmp[0] == tmp[1] and tmp[1] == tmp[2]:
        cnt += 0
    elif tmp[0] != tmp[1] and tmp[1] != tmp[2] and tmp[0] != tmp[2]:
        cnt += 0
    else:
        cnt += 1

tmp = [lst[0][0] ,lst[1][1], lst[2][2]]
if tmp[0] == tmp[1] and tmp[1] == tmp[2]:
    cnt += 0
elif tmp[0] != tmp[1] and tmp[1] != tmp[2] and tmp[0] != tmp[2]:
    cnt += 0
else:
    cnt += 1

tmp = [lst[2][0] ,lst[1][1], lst[0][2]]
if tmp[0] == tmp[1] and tmp[1] == tmp[2]:
    cnt += 0
elif tmp[0] != tmp[1] and tmp[1] != tmp[2] and tmp[0] != tmp[2]:
    cnt += 0
else:
    cnt += 1

print(cnt)