import sys

def carry_check(a, b, c):
    # 각 자리의 합이 10을 넘지 않으면 자리올림이 발생하지 않는다.
    for _ in range(4):
        if (a % 10 + b % 10 + c % 10) >= 10:
            return False
        a //= 10
        b //= 10
        c //= 10
    return True


n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

max_sum = -sys.maxsize
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            psum = lst[i] + lst[j]+ lst[k]
            if carry_check(lst[i], lst[j], lst[k]) and psum > max_sum:
                max_sum = psum

print(max_sum)