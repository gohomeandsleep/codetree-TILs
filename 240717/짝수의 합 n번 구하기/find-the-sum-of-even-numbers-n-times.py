T = int(input())

for _ in range(T):
    stp, endp = map(int, input().split())
    res = 0
    for i in range(stp, endp+1):
        if i % 2 == 0:
            res += i
    print(res)