n = int(input())

clas = 0
wall = 0
bath = 0

for i in range(1, n+1):
    if i % 12 == 0:
        bath += 1
    elif i % 3 == 0:
        wall += 1
    elif i % 2 == 0:
        clas += 1

print(clas, wall, bath)