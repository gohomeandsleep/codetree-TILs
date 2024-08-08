def push_l(lst, stp):
    tmp = lst[stp][0]
    lst[stp] = lst[stp][1:] + [tmp]
    return lst

def push_r(lst, stp):
    tmp = lst[stp][-1]
    lst[stp] = [tmp] + lst[stp][:-1]
    return lst

n, m, q = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
inst = [list(input().split()) for _ in range(q)]

for i in range(q):
    stp = int(inst[i][0]) - 1
    direction = inst[i][1]
    if direction == 'L':
        
        lst = push_r(lst, stp)
        d_up = d_down = 'L'
    else:
        lst = push_l(lst,stp)
        d_up = d_down = 'R'

    i = stp - 1
    j = stp + 1

    while i != -1: #위쪽으로 이동하면서 조건에 맞을경우 변환
        check = False
        for a in range(m):
            if lst[i][a] == lst[i+1][a]:
                check = True
        if check == False:
            break
        else:
            #print(d_up, i)
            if d_up == 'L': #오른쪽으로 밀기
                push_l(lst, i)
                d_up = 'R'
            else:
                push_r(lst, i)
                d_up = 'L'
        i -= 1
    
    while j != n: #아래쪽으로 이동하면서 조건에 맞을경우 변환
        check = False
        for a in range(m):
            if lst[j][a] == lst[j-1][a]:
                check = True
        if check == False:
            break
        else:
            if d_down == 'L': #오른쪽으로 밀기
                push_l(lst, j)
                d_down = 'R'
            else:
                push_r(lst, j)
                d_down = 'L'
        j += 1

for arr in lst:
    print(*arr, sep=' ')