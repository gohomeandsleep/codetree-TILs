n, t = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst2 = lst2[::-1]
#print(lst1, lst2)
for _ in range(t):
    tmp1 = lst1[-1]
    tmp2 = lst2[0]
    #print(tmp1, tmp2)
    lst1 = [tmp2] + lst1[:-1]
    lst2 = lst2[1:] + [tmp1]

lst2 = lst2[::-1]
print(*lst1, sep=' ')
print(*lst2, sep=' ')