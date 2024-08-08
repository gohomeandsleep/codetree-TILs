n = int(input())
lst = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

for i in range(s1-1, e1):
    lst.pop(s1-1)

for i in range(s2-1, e2):
    lst.pop(s2-1)

print(len(lst))
print(*lst, sep='\n')