n, m = map(int, input().split())
lst = list(map(int, input().split()))
sample = list(map(int, input().split()))

cnt = 0 
for i in range(n - m + 1):
    tmp = lst[i:i+m]
    if sorted(tmp) == sorted(sample):
        cnt += 1

print(cnt)