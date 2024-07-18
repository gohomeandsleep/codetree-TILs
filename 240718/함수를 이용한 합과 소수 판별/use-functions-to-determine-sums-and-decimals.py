def is_prime(a):
    if a <= 1:
        return False
    elif a <= 3:
        return True
    else:
        if a % 2 == 0:
            return False

        for i in range(3, int(a ** 0.5) + 1, 2):
            if a % i == 0:
                return False
    return True

def is_even(a):
    lst = list(str(a))
    s = 0
    for i in lst:
        s += int(i)
    if s % 2 == 0:
        return True
    else:
        return False

stp, endp = map(int, input().split())
cnt = 0
for i in range(stp, endp+1):
    if is_prime(i) == True and is_even(i) == True:
        cnt += 1
print(cnt)