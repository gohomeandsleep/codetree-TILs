num_list = list(map(int, input().split()))

for i in range(len(num_list)):
    if num_list[i] >= 250:
        num_list = num_list[:i]
        break

avg = sum(num_list) / len(num_list)
print(sum(num_list), end=' ')
print("%.1f" % avg)