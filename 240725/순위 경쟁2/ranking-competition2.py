n = int(input())
cnt = 0
lead = 2 #0-a, 1-b, 2-ab
a = b = 0
for i in range(n):
    name, score = input().split()
    if name == 'A':
        a += int(score)
    else:
        b += int(score)
    if a > b:
        if lead != 0:
            cnt += 1
        lead = 0
    elif a < b:
        if lead != 1:
            cnt += 1
        lead = 1
    else:
        if lead != 2:
            cnt += 1
        lead = 2
print(cnt)