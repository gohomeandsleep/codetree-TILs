num = int(input())
num_list = list(map(int, input().split()))

even_list = []
for i in range(len(num_list)):
    if num_list[i] % 2 == 0:
        even_list.append(num_list[i])

even_list.reverse()
for i in range(len(even_list)):
    print(even_list[i], end=' ')