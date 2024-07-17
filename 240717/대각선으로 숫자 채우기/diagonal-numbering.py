n, m = map(int, input().split())
lst = [[0] * m for _ in range(n)]
val = 1

for diag in range(n + m - 1):
    if diag < m:
        row, col = 0, diag
    else:
        row, col = diag - m + 1, m - 1
    
    while row < n and col >= 0:
        lst[row][col] = val
        val += 1
        row += 1
        col -= 1
        
for row in lst:
    print(' '.join(map(str, row)))