m, d = map(int, input().split())

lst = [31, 28, 31,30,31,30,31,31,30,31,30,31]

try:
    if d > lst[m-1]:
        print("No")
    else:
        print('Yes')
except:
    print('No')