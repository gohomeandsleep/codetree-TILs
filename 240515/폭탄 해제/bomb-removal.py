class bomb:
    def __init__(self, code, color, time):
        self.code = code
        self.color = color
        self.time = time

cd, cl, tm = input().split()
bomb1 = bomb(cd, cl, tm)

print(f"code : {bomb1.code}")
print(f"color : {bomb1.color}")
print(f"second : {bomb1.time}")