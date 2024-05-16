n = int(input())

lst = [[0 for _ in range(201)] for _ in range(201)]
offset = 100

for _ in range(n):
    stpx, stpy, endpx, endpy = map(int, input().split())
    for i in range(offset+stpx, offset+endpx):
        for j in range(offset+stpy, offset+endpy):
            lst[i][j] = 1

sumn = 0
for i in range(201):
    sumn += sum(lst[i])

print(sumn)