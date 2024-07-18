n1, n2 = map(int, input().split())

lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

r = 'No'
for i in range(n1 - n2 + 1):
    #print(lst1[i:i+n2], lst2)
    if lst1[i:i+n2] == lst2:
        r = 'Yes'

print(r)