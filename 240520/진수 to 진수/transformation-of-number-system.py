a, b = map(int, input().split())

num_list = list(map(int, list(input())))
leng = len(num_list)
#a진수 -> 10진수
num = 0
for i in range(leng):
    num = num * a + num_list[i]

#10진수 -> b진수
res_list = []
while num >= b:
    res_list.append(num % b)
    num = num // b
res_list.append(num)

print(*res_list[::-1], sep='')