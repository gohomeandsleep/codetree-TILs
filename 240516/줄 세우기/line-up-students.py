class students:
    def __init__(self, height, weight, number):
        self.height = height
        self.weight = weight
        self.number = number

n = int(input())
std_list = []
for i in range(n):
    h, w = map(int, input().split())
    student = students(h, w, i+1)
    std_list.append(student)

std_list.sort(key=lambda x:(-x.height, -x.weight, x.number))

for num in std_list:
    print(num.height, num.weight, num.number)