lst = list(map(int, input().split()))
team3 = max(lst)
lst.remove(team3)

res = float('inf')
for i in range(4):
    for j in range(4):
        if i == j:
            continue
        team1 = lst[i] + lst[j]
        team2 = sum(lst) - lst[i] - lst[j]
        if team1 == team2 or team2 == team3 or team1 == team3:
            continue
        tmp = max(team1, team2, team3) - min(team1, team2, team3)
        res = min(res, tmp)
if res == float('inf'):
    print(-1)
else:
    print(res)