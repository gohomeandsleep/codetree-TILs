n = int(input())
lst = list(map(int, input().split()))

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if abs(lst[0] - i) <= 2 or abs(lst[1] - j) <= 2 or abs(lst[2] - k) <= 2:
                cnt += 1

print(cnt)