n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

m = float('inf')
for i in range(1, 101): #x좌표
    for j in range(1, 101): #y좌표
        section1 = section2 = section3 = section4 = 0
        for k in range(n):
            if lst[k][0] < i:
                if lst[k][1] < j:
                    section1 += 1
                else:
                    section2 += 1
            else:
                if lst[k][1] < j:
                    section3 += 1
                else:
                    section4 += 1
        m = min(m, max(section1, section2, section3, section4))
print(m)