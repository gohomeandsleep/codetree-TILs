from datetime import datetime

m1, d1, m2, d2 = map(int, input().split())

base_date = datetime(2011, 1, 1)

date1 = datetime(2011, m1, d1)
date2 = datetime(2011, m2, d2)

# 두 날짜의 차이를 계산
date_diff = (date2 - date1).days

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(day[date_diff % 7])