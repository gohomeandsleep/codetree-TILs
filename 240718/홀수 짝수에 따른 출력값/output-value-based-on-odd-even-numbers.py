n = int(input())
lst = [i+1 for i in range(n)]

res = 0
if n % 2 != 0:
    for i in lst:
        if i % 2 != 0:
            res += i
    print(res)
else:
    for i in lst:
        if i % 2 == 0:
            res += i
    print(res)