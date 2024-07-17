n1, n2 = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
res = 'No'
for i in range(n1 - n2 + 1):
    if lst2 == lst1[i:i+n2]:
        res = 'Yes'

print(res)