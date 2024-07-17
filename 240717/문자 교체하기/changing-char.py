a, b = list(input().split())

print(*a[:2], sep='', end='')
print(*b[2:], sep='')