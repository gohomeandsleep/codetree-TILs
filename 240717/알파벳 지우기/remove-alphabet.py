lst1 = list(input())
lst2 = list(input())

lst1 = [ch for ch in lst1 if '0' <= ch <= '9']
lst2 = [ch for ch in lst2 if '0' <= ch <= '9']

res1 = int("".join(lst1))
res2 = int("".join(lst2))
print(res1 + res2)