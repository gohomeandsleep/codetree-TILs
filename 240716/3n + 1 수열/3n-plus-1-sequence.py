n = int(input())
res = 0
while True:
    if n == 1:
        break
    elif n % 2 == 0:
        n //= 2
    else:
        n = n * 3 + 1
    res += 1

print(res)