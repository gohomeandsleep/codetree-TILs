N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]

max = 0
for i in range(N):
    for j in range(1, N-1):
        sum = lst[i][j-1] + lst[i][j] + lst[i][j+1]
        if sum > max:
            max = sum

print(max)