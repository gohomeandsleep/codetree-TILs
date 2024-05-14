num_list = list(map(int, input().split()))

for i in range(len(num_list)):
    if num_list[i] == 0:
        num_list = num_list[:i]
        break

two = []

for i in range(len(num_list)):
    if num_list[i] % 2 == 0:
        two.append(num_list[i])

print(len(two), sum(two))