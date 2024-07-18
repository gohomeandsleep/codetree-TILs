n = int(input())
lst = list(map(int,input().split()))

for i in range(1, n+1, 2):
    tmp = lst[:i+1]
    tmp.sort()
    print(tmp[i//2], end=' ')