a, b, c = map(int, input().split())
res = False
for i in range(a, b+1):
    if i % c == 0:
        res = True

if res == True:
    print('YES')
else:
    print('NO')