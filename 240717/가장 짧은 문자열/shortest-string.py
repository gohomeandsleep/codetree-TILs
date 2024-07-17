lst = [input() for _ in range(3)]

length = []
for i in range(3):
    length.append(len(lst[i]))

print(max(length) - min(length))