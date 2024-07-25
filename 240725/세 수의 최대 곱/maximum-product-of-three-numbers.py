n = int(input())
minus = []
plus = []
zero = []
lst = list(map(int, input().split()))
for i in range(n):
    k = lst[i]
    if k > 0:
        plus.append(k)
    elif k == 0:
        zero.append(0)
    else:
        minus.append(k)

plus.sort()
minus.sort(reverse=True)

res = 1
if len(minus) == 0:
    if len(plus) < 3:
        print(0)
    else:
        tmp = plus[-3:]
        for i in range(3):
            res *= tmp[i]
        print(tmp)
elif len(minus) == 1:
    if len(plus) < 3:
        if len(zero) > 0:
            print(0)
        else:
            for i in range(2):
                res *= plus[i]
            res *= minus[0]
            print(res)
else:
    if len(plus) == 0:
        print(0)
    elif len(plus) < 3:
        for j in range(2):
            res *= minus[j]
        res *= max(plus)
        print(res)
    else:
        case1 = plus[-3:]
        res1 = 1
        for i in range(3):
            res1 *= case1[i]

        case2_p = max(plus)
        case2_n = minus[-2:]
        res2 = 1
        for i in range(2):
            res2 *= case2_n[i]
        res2 *= case2_p

        print(max(res1, res2))