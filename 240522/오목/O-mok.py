lst = [list(map(int, input().split())) for _ in range(19)]

for i in range(19):
    for j in range(19):
        if lst[i][j] != 0:
            primary = lst[i][j]
            #case1. 직선으로 같을때
            if lst[i][j+1] == primary and lst[i][j+2] == primary and lst[i][j+3] == primary and lst[i][j+4] == primary:
                print(primary)
                print(i+1, j+3)
            if lst[i+1][j] == primary and lst[i+2][j] == primary and lst[i+3][j] == primary and lst[i+4][j] == primary:
                print(primary)
                print(i+3, j+1)
            if lst[i+1][j+1] == primary and lst[i+2][j+2] == primary and lst[i+3][j+3] == primary and lst[i+4][j+4] == primary:
                print(primary)
                print(i+3, j+3)
            if lst[i+1][j-1] == primary and lst[i+2][j-2] == primary and lst[i+3][j-3] == primary and lst[i+4][j-4] == primary:
                print(primary)
                print(i+3, j-1)