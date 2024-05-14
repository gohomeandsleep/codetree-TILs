num_list = list(map(int, input().split()))

for i in range(len(num_list)):
    if num_list[i] == 0:
        num_list = num_list[:i]
        break

for i in range(len(num_list)):
    print(num_list[len(num_list)-i-1], end=' ')