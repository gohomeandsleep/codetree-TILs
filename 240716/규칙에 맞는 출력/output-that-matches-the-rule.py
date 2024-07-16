n = int(input())

lst = [i+1 for i in range(n)]
for i in range(n-1, -1, -1):
    tmp = lst[i:]
    print(*tmp, sep=' ')