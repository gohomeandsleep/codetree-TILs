n, k = map(int, input().split())
lst = list(map(int, input().split()))

m = lst[0]
while len(lst) > 1:
    min_t = min(lst[1:k+1])
    #print(lst[1:k+1])
    min_k = lst.index(min_t)
    m = max(m, min_t)
    lst = lst[min_k:]
    #print(min_t)
print(m)