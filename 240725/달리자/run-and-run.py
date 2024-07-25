n = int(input())
start = list(map(int, input().split()))
end = list(map(int, input().split()))
res = 0
for i in range(n-1):
    if start[i] > end[i]:
        res += start[i] - end[i]
        start[i+1] += start[i] - end[i]
print(res)