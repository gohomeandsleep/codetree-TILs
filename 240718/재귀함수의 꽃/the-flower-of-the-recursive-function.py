n = int(input())

lst1 = [n-i for i in range(n)]
lst2 = [i+1 for i in range(n)]

print(*lst1, sep=' ', end=' ')
print(*lst2, sep=' ')