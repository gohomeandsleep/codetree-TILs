T, k, check = input().split()
check = list(check)

lst = []
for _ in range(int(T)):
    tmp = input()
    tmpl = list(tmp)
    if tmpl[:len(check)] == check:
        lst.append(tmp)

lst.sort()
print(lst[int(k)-1])