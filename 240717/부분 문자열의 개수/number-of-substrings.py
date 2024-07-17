lst = list(input())
c = list(input())

stat = 0
for i in range(len(lst) - len(c) + 1):
    if lst[i:i+len(c)] == c:
        stat += 1

print(stat)