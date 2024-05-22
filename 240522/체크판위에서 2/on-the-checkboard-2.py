height, width = map(int, input().split())

lst = [list(input().split()) for _ in range(height)]

first = lst[0][0]
other = lst[height-1][width-1]

cnt = 0
for i in range(1, height):
    for j in range(1, width):
        if lst[i][j] == other:
            for k in range(i, height-i):
                for l in range(j, width-j):
                    if lst[k][l] == first:

                        cnt +=1

print(cnt)
# max_cnt = 0
# for i in range(n):
#     for j in range(n - 1):
#         for k in range(i + 1, n):
#             for l in range(n - 1):
#                 max_cnt = max(max_cnt, arr[i][j] + arr[i][j + 1]
#                                      + arr[k][l] + arr[k][l + 1])

# print(max_cnt)