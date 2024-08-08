n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
y, x = map(int, input().split())
r = lst[y-1][x-1] - 1  # The blast radius excluding the bomb's own cell
lst[y-1][x-1] = 0

def in_range(y, x):
    return 0 <= y < n and 0 <= x < n

for i in range(-r, r + 1):
    for j in range(-r, r + 1):
        if in_range(y - 1 + i, x - 1 + j):
            if abs(i) + abs(j) <= r:
                if i == 0 or j == 0: 
                    lst[y - 1 + i][x - 1 + j] = 0

for i in range(n):
    tmp_lst = []
    for j in range(n-1, -1, -1):
        tmp_lst.append(lst[j][i])
    
    real = []
    zero = 0
    for j in range(n):
        if tmp_lst[j] != 0:
            real.append(tmp_lst[j])
        else:
            zero += 1
    tmp_lst = real + [0 for _ in range(zero)]
    for j in range(n):
        lst[n-j-1][i] = tmp_lst[j]

for arr in lst:
    print(*arr, sep=' ')