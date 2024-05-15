n = int(input())

num_list = [n*(i+1) for i in range(10)]

div5 = 0

for num in num_list:
    print(num, end=' ')
    if num % 5 == 0:
        div5 +=1
    if div5 == 2:
        break