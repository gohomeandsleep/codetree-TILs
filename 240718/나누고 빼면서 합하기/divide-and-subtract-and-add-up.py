n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst = [0] + lst
res = 0
while m != 0:
    res += lst[m]
    if m % 2 == 0:
        m //= 2
    else:
        m -= 1

print(res)