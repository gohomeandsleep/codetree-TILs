def is_prime(a):
    if a < 2:
        return False
    else:
        for i in range(3, int(a ** 0.5) + 1, 2):
            if a % i == 0:
                return False
    return True

stp, endp = map(int, input().split())

res = 0
for i in range(stp, endp + 1):
    if is_prime(i) == True:
        res += i

print(res)