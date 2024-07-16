prim = int(input())
n = prim
lst = []
freq = []
while n % 2 == 0:
    if 2 not in lst:
        lst.append(2)
        freq.append(1)
    else:
        freq[0] += 1
    n //= 2

for i in range(3, int(n ** 0.5), 2):
    if n % i == 0:
        if i not in lst:
            lst.append(i)
            freq.append(1)
        else:
            freq[lst.index(i)] += 1
        n //= i

if n > 2:
    lst.append(n)
    freq.append(1)

res = 1
for i in range(len(lst)):
    tmp = 1
    for j in range(1, freq[i]+1):
        tmp += lst[i] ** j
    res *= tmp

if res // 2 == prim:
    print('P')
else:
    print('N')