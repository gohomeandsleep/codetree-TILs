n = int(input())

lst = [1, 2]
for i in range(n - 2):
    lst.append(lst[-1] + lst[i // 3])

print(lst[-1])