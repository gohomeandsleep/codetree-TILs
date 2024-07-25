n, k = map(int, input().split())
lst = [int(input()) for _ in range(n)]

res = {}
for i in range(n):
    tmp_k = lst[i]
    tmp_l = lst[i+1:i+1+k]
    if tmp_l.count(tmp_k) > 0:
        if tmp_k in res:
            res[tmp_k] += 1
        else:
            res[tmp_k] = 2
max_value_key = max(res, key=res.get)
print(max_value_key)