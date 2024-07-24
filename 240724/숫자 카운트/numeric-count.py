n = int(input())
condition = []
for _ in range(n):
    num, s, b = map(int, input().split())
    condition.append([num // 100, (num // 10) % 10, num % 10, s, b])

res = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue
            tmp = [i, j, k]
            valid = True
            for cond in condition:
                strike = 0
                ball = 0
                for m in range(3):
                    if cond[m] == tmp[m]:
                        strike += 1
                    elif cond[m] in tmp:
                        ball += 1
                if strike != cond[3] or ball != cond[4]:
                    valid = False
                    break
            if valid:
                res += 1
print(res)