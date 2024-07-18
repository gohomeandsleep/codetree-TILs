n = int(input())

lst = [i+1 for i in range(n)]
print(*lst, sep=' ')
lst = lst[::-1]

print(*lst, sep=' ')