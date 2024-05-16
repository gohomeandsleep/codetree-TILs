ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
mx1, my1, mx2, my2 = map(int, input().split())

lst = [[0 for _ in range(2000)] for _ in range(2000)]
offset = 1000

for i in range(offset+ax1, offset+ax2):
    for j in range(offset+ay1, offset+ay2):
        lst[i][j] = 1

for i in range(offset+bx1, offset+bx2):
    for j in range(offset+by1, offset+by2):
        lst[i][j] = 1

for i in range(offset+mx1, offset+mx2):
    for j in range(offset+my1, offset+my2):
        lst[i][j] = 0

sumn = 0
for i in range(2000):
    sumn += sum(lst[i])

print(sumn)