height, width = map(int, input().split())

lst = [list(input().split()) for _ in range(height)]

first = lst[0][0]
other = lst[height-1][width-1]

cnt = 0
for i in range(1,height-1):
    for j in range(1, width-1):
        if lst[i][j] == other:
            #print(i, j, end='\n----------\n')
            for k in range(i+1, height-1):
                for l in range(j+1, width-1):
                    if lst[k][l] == first:
                        #print(k, l, cnt+1)
                        cnt += 1
print(cnt)