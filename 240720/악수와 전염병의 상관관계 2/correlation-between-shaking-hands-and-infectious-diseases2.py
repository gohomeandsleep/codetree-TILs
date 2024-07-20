n, k, p, T = map(int, input().split())
#악수한 순서 시간순서로 정렬
lst = []
for _ in range(T):
    t, a, b = map(int, input().split())
    lst.append([t, a, b])
lst = sorted(lst, key = lambda x:x[0])


#결과와 타이머 설정해서 처음 전염병에 걸린 개발자를 추가
res = [0 for _ in range(n)]
timer = [0 for _ in range(n)]
res[p-1] = 1
timer[p-1] = k

for i in range(T):
    a = lst[i][1]
    b = lst[i][2]
    if res[a-1] == 1 and timer[a-1] >= 1:
        if res[b-1] == 0:
            res[b-1] = 1
            timer[b-1] = k
        timer[a-1] -= 1
    elif res[b-1] == 1 and timer[b-1] >= 1:
        if res[a-1] == 0:
            res[a-1] = 1
            timer[a-1] = k
        timer[b-1] -= 1

print(*res, sep='')