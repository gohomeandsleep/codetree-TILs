import sys

n = int(input())
lst = list(map(int, input().split()))
max = -sys.maxsize
for i in range(n):
    #i : 첫번째 인자
    for j in range(i+2, n):
        #j : 두번째 인자
        #print(lst[i] + lst[j])
        if lst[i] + lst[j] > max:
            max = lst[i] + lst[j]

print(max)