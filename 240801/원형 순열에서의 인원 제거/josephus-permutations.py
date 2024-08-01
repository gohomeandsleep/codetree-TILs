n, k = map(int, input().split())

lst = [i+1 for i in range(n)]
cur = k-1

for i in range(n):
  print(lst[cur], end="")
  lst.pop(cur)
  try:
    cur = (cur + k -1) % len(lst)
    print(" ", end='')
  except:
    break