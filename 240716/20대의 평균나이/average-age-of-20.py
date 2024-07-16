lst = []
while True:
    n = int(input())
    if n > 19 and n < 30:
        lst.append(n)
    else:
        break

print("%.2f" % (sum(lst) / len(lst)))