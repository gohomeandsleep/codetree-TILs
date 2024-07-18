n = int(input())
lst = list(str(n))
#print(lst)
res = 0
for i in lst:
    res += int(i)
if n % 2 == 0 and res % 5 == 0:
    print('Yes')
else:
    print('No')