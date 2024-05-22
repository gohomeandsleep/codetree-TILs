import sys

n = int(input())

num_lst = list(map(int, input().split()))

min_len = None
for i in range(n):
    len = 0
    for j in range(n):
        len += num_lst[j] * abs(j-i)
    if min_len == None or min_len > len:
        min_len = len

print(min_len)