def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

a, b = map(int, input().split())

res = False
for i in range(a, b+1):
    if gcd(i, 1920) != 1 and gcd(i, 2880) != 1:
        res = True

if res == True:
    print(1)
else:
    print(0)