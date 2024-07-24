k, n = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(k)]

rank = []
for i in range(n):
    for j in range(n):
        if i >= j:
            continue
        rank.append([lst[0][i], lst[0][j]])

for i in range(1, k):
    compare = []
    for j in range(n):
        for l in range(n):
            if j >= l:
                continue
            compare.append([lst[i][j], lst[i][l]])
    new_rank = []
    for item in rank:
        if item in compare:
            new_rank.append(item)
    
    rank = new_rank
print(len(rank))