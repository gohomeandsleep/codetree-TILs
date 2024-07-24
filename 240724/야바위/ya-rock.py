T = int(input())
lst = [list(map(int, input().split())) for _ in range(T)]
mxm = 0

case1 = [1, 0, 0]
cnt = 0
for i in range(T):
    case1[lst[i][0] - 1], case1[lst[i][1] - 1] = case1[lst[i][1] - 1], case1[lst[i][0] - 1]
    if case1[lst[i][2] - 1] == 1:
        cnt += 1
mxm = max(mxm, cnt)

case2 = [0, 1, 0]
cnt = 0
for i in range(T):
    case2[lst[i][0] - 1], case2[lst[i][1] - 1] = case2[lst[i][1] - 1], case2[lst[i][0] - 1]
    if case2[lst[i][2] - 1] == 1:
        cnt += 1
mxm = max(mxm, cnt)

case3 = [0, 0, 1]
cnt = 0
for i in range(T):
    case3[lst[i][0] - 1], case3[lst[i][1] - 1] = case3[lst[i][1] - 1], case3[lst[i][0] - 1]
    if case3[lst[i][2] - 1] == 1:
        cnt += 1
mxm = max(mxm, cnt)

print(mxm)