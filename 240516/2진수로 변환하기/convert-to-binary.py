n = int(input())

digit = []

while True:
    if n < 2:
        digit.append(n)
        break
    else:
        digit.append(n % 2)
        n = n // 2

print(*digit[::-1], sep='')