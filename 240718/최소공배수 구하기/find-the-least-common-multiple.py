def gcd (a,b):
    while b:
        a, b = b, a % b
    return a

n, m = map(int, input().split())
print(n * m // gcd(n, m))