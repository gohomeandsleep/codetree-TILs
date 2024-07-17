n = int(input())
lst = list(map(int, input().split()))

lst.sort(reverse=True)
print(lst[0], lst[1])