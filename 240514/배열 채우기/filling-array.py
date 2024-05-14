num_list = list(map(int, input().split()))

for i in range(len(num_list) -1):
    print(num_list[len(num_list) - i - 2], end=' ')