prim = int(input())
n = prim
lst = set()
lst.add(1)
while n % 2 == 0:
    lst.add(2)
    n //= 2

for i in range(3, int(n ** 0.5) + 1, 2):
    if n % i == 0:
        lst.add(i)
        n //= i

if n > 2:
    lst.add(n)

if sum(lst) == prim:
    print('P')
else:
    print('N')