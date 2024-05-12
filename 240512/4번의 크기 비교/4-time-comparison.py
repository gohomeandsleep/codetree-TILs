a = int(input())

num_list = list(map(int, input().split()))

for i in range(len(num_list)):
    if a > num_list[i]:
        print(1)
    else:
        print(0)