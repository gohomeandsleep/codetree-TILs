lst = []
x = []
y = []

for i in range(10):
    line = list(input())
    for j in range(10):
        if line[j] != '.':
            lst.append(line[j])
            x.append(j)
            y.append(i)

shortest = abs(x[lst.index('L')] - x[lst.index('B')]) + abs(y[lst.index('L')] - y[lst.index('B')]) - 1

if x[0] == x[1] and x[1] == x[2]:
    if y[lst.index('L')] < y[lst.index('R')] < y[lst.index('B')] or y[lst.index('L')] > y[lst.index('R')] > y[lst.index('B')]:
        shortest += 2

if y[0] == y[1] and y[1] == y[2]:
    if x[lst.index('L')] < x[lst.index('R')] < x[lst.index('B')] or x[lst.index('L')] > x[lst.index('R')] > x[lst.index('B')]:
        shortest += 2

print(shortest)