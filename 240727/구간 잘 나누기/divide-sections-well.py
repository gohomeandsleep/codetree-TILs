n, k = map(int, input().split())
lst = list(map(int, input().split()))

max_sum = 10001

for i in range(max(lst), max_sum):
    part = 1  # 구간의 개수
    p_sum = 0  # 부분합

    for j in range(n):
        if p_sum + lst[j] > i:
            part += 1
            p_sum = 0
        p_sum += lst[j]

    if part <= k:
        print(i)
        break