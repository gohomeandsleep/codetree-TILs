import sys

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

min_sum = sys.maxsize
for i in range(n):
    #i : 시작할 방
    sum = 0
    for j in range(n-1):
        try:
            sum += (j+1) * lst[i+j+1]
            #print((j+1) * lst[i+j+1], end=' ')
        except:
            sum += (j+1) * lst[i+j+1-n]
            #print((j+1) * lst[i+j+1-n], end=' ')
    #print(sum)

    if sum < min_sum:
        min_sum = sum
        #print(sum)

print(min_sum)