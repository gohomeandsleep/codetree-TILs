n = int(input())

for i in range(2, n+1):
    stat = True
    for j in range(2, int((i**0.5))+1):
        if i % j == 0:
            stat = False
    if stat == True:
        print(i, end=' ')