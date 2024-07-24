def intersection(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    
    intersection = set1 & set2
    return len(intersection) > 0

n = int(input())
lst = []
for _ in range(n):
    x, y = map(int, input().split())
    lst.append([x, y+11])

stat = 0
for i in range(22):
    for j in range(22):
        for k in range(22):
            tmp = [i, j, k]
            cnt = 0
            for l in range(n):
                if intersection(tmp, lst[l]):
                    cnt += 1
            if cnt == n:
                stat = 1

print(stat)