num_list = list(map(int, input().split()))

for i in range(len(num_list)):
    if num_list[i] == 0:
        num_list = num_list[:i]
        break

print("%d %.1f" % (sum(num_list), sum(num_list) / len(num_list)))