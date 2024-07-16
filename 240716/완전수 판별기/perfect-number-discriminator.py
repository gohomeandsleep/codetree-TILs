prim = int(input())
n = prim
lst = [1]
while n % 2 == 0:
    lst.append(2)
    n //= 2

for i in range(3, int(n ** 0.5) + 1, 2):
    if n % i == 0:
        lst.append(i)
        n //= i

if n > 2:
    lst.append(n)

if sum(lst) == prim:
    print('P')
else:
    print('N')