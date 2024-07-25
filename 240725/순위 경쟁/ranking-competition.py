n = int(input())
cnt = 0
lead = 7 #0-a, 1-b, 2-c, 3-ab, 4-ac, 5-bc, 6-abc
a = b = c = 0
for i in range(n):
    name, score = input().split()

    if name == 'A':
        a += int(score)
    elif name == 'B':
        b += int(score)
    else:
        c += int(score)

    if a > b and a > c:
        if lead != 0:
            cnt += 1
        lead = 0
    elif b > a and b > c:
        if lead != 1:
            cnt += 1
        lead = 1  
    elif c > a and c > b:
        if lead != 2:
            cnt += 1
        lead = 2
    elif a == b and a > c:
        if lead != 3:
            cnt += 1
        lead = 3
    elif a == c and a > b:
        if lead != 4:
            cnt += 1
        lead = 4
    elif c == b and b > a:
        if lead != 5:
            cnt += 1
        lead = 5
    elif a == b and a == c:
        if lead != 6:
            cnt += 1
        lead = 6        
print(cnt)