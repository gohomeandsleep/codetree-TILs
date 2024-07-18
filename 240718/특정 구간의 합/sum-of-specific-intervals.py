n, T = map(int, input().split())
lst = list(map(int, input().split()))

for _ in range(T):
    stp, endp = map(int, input().split())
    res = 0
    for i in range(stp-1, endp ):
        res += lst[i]
    print(res)