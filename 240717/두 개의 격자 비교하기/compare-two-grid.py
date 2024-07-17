n, m = map(int, input().split())
lst1 = [list(map(int, input().split())) for _ in range(n)]
lst2 = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if lst1[i][j] == lst2[i][j]:
            print(0, end=' ')
        else:
            print(1, end=' ')
    print('')