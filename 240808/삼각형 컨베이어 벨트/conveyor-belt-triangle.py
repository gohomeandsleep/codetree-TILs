n, t = map(int, input().split())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))
lst3 = list(map(int, input().split()))
#print(lst1, lst2)
for _ in range(t):
    tmp1 = lst1[-1]
    tmp2 = lst2[-1]
    tmp3 = lst3[-1]
    #print(tmp1, tmp2)
    lst1 = [tmp3] + lst1[:-1]
    lst2 = [tmp1] + lst2[:-1]
    lst3 = [tmp2] + lst3[:-1]

print(*lst1, sep=' ')
print(*lst2, sep=' ')
print(*lst3, sep=' ')