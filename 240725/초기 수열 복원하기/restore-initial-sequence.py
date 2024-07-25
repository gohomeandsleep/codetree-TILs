n = int(input())
lst = list(map(int, input().split()))

for i in range(1, 1001):
    tmp = [i]
    for j in range(n-1):
        nxt = lst[j] - tmp[-1] 
        if nxt < 1 or nxt in tmp:
            break
        else:
            tmp.append(lst[j] - tmp[-1])
    if len(tmp) == n:
        print(*tmp, sep=' ')