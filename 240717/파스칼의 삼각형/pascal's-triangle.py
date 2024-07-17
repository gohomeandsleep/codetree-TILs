n = int(input())

if n >= 1:
    print(1)
if n >= 2:
    print('1 1')
if n >= 3:
    prev = [1, 1]
    for i in range(3, n+1):
        #print(prev)
        lst = [1]
        for j in range(i-2):
            lst.append(prev[j] + prev[j+1])
        lst.append(1)
        print(*lst, sep=' ')
        prev = lst