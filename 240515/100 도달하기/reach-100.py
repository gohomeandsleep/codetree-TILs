n = int(input())

first = 1
second = n
print(first, second, end=' ')
while first<100 and second<100:
    first = first + second
    print(first, end=' ')
    first, second = second, first