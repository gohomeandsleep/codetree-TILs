lst = list(map(int, input().split()))

gap = max(lst[1] - lst[0], lst[2] - lst[1])
print(gap - 1)