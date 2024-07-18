n = int(input())
for _ in range(n):
    d, t, w = input().split()
    if w == 'Rain':
        print(d, t, w)
        break