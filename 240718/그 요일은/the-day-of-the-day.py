from datetime import datetime

m1, d1, m2, d2 = map(int, input().split())
rest_d = input()

base_date = datetime(2011, 1, 1)

date1 = datetime(2024, m1, d1)
date2 = datetime(2024, m2, d2)

date_diff = (date2 - date1).days

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
rest = day.index(rest_d)
#print(rest, date_diff)
res = 0
for i in range(abs(date_diff)+ 1):
    if i % 7 == rest:
        res += 1
print(res)