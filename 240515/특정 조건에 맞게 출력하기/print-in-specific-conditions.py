num_list = list(map(int, input().split()))

for num in num_list:
    if num == 0:
        break
    elif num % 2 ==0:
        print(num // 2, end=' ')
    else:
        print(num + 3, end=' ')