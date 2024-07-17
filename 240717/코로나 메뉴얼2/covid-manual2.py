lst = []
res = [0 for _ in range(4)]
for _ in range(3):
    cold, t = input().split()
    if cold == 'Y' and int(t) >= 37:
        res[0] += 1
    elif cold == 'N' and int(t) >= 37:
        res[1] += 1
    elif cold == 'Y':
        res[2] += 1
    else:
        res[3] += 1

print(*res, sep=' ', end=' ')
if res[0] >= 2:
    print("E")