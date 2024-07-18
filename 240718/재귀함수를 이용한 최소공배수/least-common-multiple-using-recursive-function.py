def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

n = int(input())
lst = list(map(int, input().split()))

a = lst[0]
for i in range(1, n):
    b = lst[i]
    a = a * b // gcd(a, b)

print(a)