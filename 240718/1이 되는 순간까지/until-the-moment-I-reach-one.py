n = int(input())

cnt = 0
while n != 1:
    if n % 2 == 0:
        n //= 2
    else:
        n //= 3
    cnt += 1

print(cnt)