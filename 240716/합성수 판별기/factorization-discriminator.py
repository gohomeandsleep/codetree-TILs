n = int(input())

res = True
for i in range(2, n):
    if n % i == 0:
        res = False

if res == True:
    print('N')
else:
    print('C')