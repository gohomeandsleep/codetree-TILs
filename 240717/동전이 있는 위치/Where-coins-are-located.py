n, m = map(int, input().split())
lst = []
for _ in range(m):
    x, y = map(int, input().split())
    lst.append([x-1, y-1])

for i in range(n):
    for j in range(n):
        if [i,j] in lst:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print('')