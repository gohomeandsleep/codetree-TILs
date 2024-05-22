import sys

checkpoint = int(input())
lstx = []
lsty = []
for i in range(checkpoint):
    x, y = input().split()
    lstx.append(int(x))
    lsty.append(int(y))

min_len = sys.maxsize
for i in range(1, checkpoint-1):
    len = 0
    #i = skip하는 checkpoint
    for j in range(0, checkpoint-1):
        if j+1 == i: 
            #print(lstx[j] , lstx[j+2] ,lsty[j] ,lsty[j+2])
            len += abs(lstx[j] - lstx[j+2]) + abs(lsty[j] - lsty[j+2])
            #print(len)
        elif j == i:
            continue
        else:
            #print(lstx[j] , lstx[j+1] ,lsty[j] ,lsty[j+1])
            len += abs(lstx[j] - lstx[j+1]) + abs(lsty[j] - lsty[j+1])
            #print(len)
    #print(len, end='\n--------------------\n')
    if min_len > len:
        min_len = len

print(min_len)