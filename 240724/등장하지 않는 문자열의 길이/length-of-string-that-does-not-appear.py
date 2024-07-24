def sublist(a,b):
    n, m = len(a), len(b)
    for i in range(n -m + 1):
        if a[i:i+m] == b:
            return True
    return False

n = int(input())
lst = list(input())

mxm = 0
for i in range(n):
    for j in range(i+1, n):
        tmp = lst[i:j+1]
        #print(tmp, lst[j+1:])
        if sublist(lst[j+1:], tmp) and len(lst[j+1:]) > 0:
            #print(len(tmp))
            mxm = max(mxm, len(tmp))

print(mxm + 1)