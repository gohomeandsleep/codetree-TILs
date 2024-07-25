a, b, x, y = map(int, input().split())

route1 = abs(a - b)
route2 = abs(a - x) + abs(b - y)
route3 = abs(a - y) + abs(b - x)

print(min(route1, route2, route3))