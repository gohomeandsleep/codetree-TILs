def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())

res = False
for i in range(a, b+1):
    if gcd(i, 960) != 1:
        res = True

if res == True:
    print(1)
else:
    print(0)