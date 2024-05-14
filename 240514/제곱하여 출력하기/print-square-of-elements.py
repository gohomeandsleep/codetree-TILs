num = int(input())

num_list = list(map(int, input().split()))

for i in range(len(num_list)):
    print(num_list[i] ** 2, end=' ')