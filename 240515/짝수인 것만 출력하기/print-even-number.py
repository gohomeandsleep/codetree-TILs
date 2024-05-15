input()
num_list = list(map(int, input().split()))

for num in num_list:
    if num % 2 == 0: print(num, end=' ')