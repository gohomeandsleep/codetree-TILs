a, b = input().split()
a = list(a)

try:
    print(a.index(b))
except:
    print('No')