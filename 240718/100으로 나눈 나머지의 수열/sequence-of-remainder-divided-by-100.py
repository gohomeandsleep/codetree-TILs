n = int(input())

a = 2
b = 4
for i in range(n-2):
    tmp = a * b % 100
    a, b = b, tmp
    #print(a,b)

if n == 1:
    print(a)
else:
    print(b)