lst1 = [list(map(int, input().split())) for _ in range(3)]
tmp = input()
lst2 = [list(map(int, input().split())) for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(lst1[i][j] * lst2[i][j], end=' ')
    print('')