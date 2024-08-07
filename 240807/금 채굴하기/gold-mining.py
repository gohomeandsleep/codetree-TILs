l, coin = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(l)]

res = 0

for i in range(l): #기준점 세로
    for j in range(l): #기준점 가로
        for k in range(2 * (l - 1)): #기준점과의 거리
            cost = k ** 2 + (k + 1) ** 2
            p_sum = 0
            for m in range(l): #비교점 세로
                for n in range(l): #비교점 가로
                    dist = abs(i - m) + abs(j - n)
                    if k >= dist:
                        p_sum += lst[m][n]
            if p_sum * coin >= cost:
                res = max(res, p_sum)

print(res)