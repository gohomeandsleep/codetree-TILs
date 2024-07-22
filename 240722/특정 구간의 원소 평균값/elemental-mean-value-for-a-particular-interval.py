n = int(input())
lst = list(map(int, input().split()))

cnt = len(lst)
for i in range(n):
    for j in range(i+1, n):
        avg = sum(lst[i:j+1]) // len(lst[i:j+1])
        if avg in lst[i:j+1] and sum(lst[i:j+1]) % len(lst[i:j+1]) == 0:
            cnt += 1

print(cnt)