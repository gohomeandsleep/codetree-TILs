n = int(input())

i = 1
res = 1
while n > res:
    res *= i
    i += 1
    
print(i-1)