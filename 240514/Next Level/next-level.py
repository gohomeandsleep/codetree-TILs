class Level:
    def __init__(self, id='codetree', level = 10):
        self.id = id
        self.level = level


level1 = Level()
id, level = input().split()
level2 = Level(id, level)

print(f"user {level1.id} lv {level1.level}")
print(f"user {level2.id} lv {level2.level}")