T, a, b = map(int, input().split())
lst = []
end = 0
for _ in range(T):
    t, l = input().split()
    end = max(end, int(l))
    lst.append([t, int(l)])

loc = [' ' for _ in range(end + 1)]
for i in range(T):
    loc[lst[i][1]] = lst[i][0]

res = 0
for i in range(a, b + 1):
    left_S = left_N = float('inf')
    for j in range(i, -1, -1):
        if loc[j] == 'S':
            left_S = i - j
            break
    for j in range(i, -1, -1):
        if loc[j] == 'N':
            left_N = i - j
            break
    
    right_S = right_N = float('inf')
    for j in range(i, end + 1):
        if loc[j] == 'S':
            right_S = j - i
            break
    for j in range(i, end + 1):
        if loc[j] == 'N':
            right_N = j - i
            break
    
    S = min(left_S, right_S)
    N = min(left_N, right_N)
    
    if S <= N:
        res += 1

print(res)