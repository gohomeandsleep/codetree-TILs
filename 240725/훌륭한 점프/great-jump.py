n, k = map(int, input().split())
lst = list(map(int, input().split()))

m = lst[0]
while len(lst) > 1:
    slice_end = min(len(lst), k + 1)
    min_t = min(lst[1:slice_end])
    min_k = lst[1:slice_end].index(min_t) + 1

    m = max(m, min_t)
    lst = lst[min_k:]

print(m)