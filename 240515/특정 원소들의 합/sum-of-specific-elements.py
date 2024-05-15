num_list = [list(map(int, input().split())) for _ in range(4)]

sum = 0
for i in range(4):
    for j in range(4):
        if i >= j:
            sum += num_list[i][j]

print(sum)