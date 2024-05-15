class information:
    def __init__(self, name, address, location):
        self.name = name
        self.address = address
        self.location = location

info_list = []

n = int(input())
for _ in range(n):
    nm, ad, lc = input().split()
    info_list.append(information(nm, ad, lc))

info_list.sort(key=lambda x: x.name)

print(f"name {info_list[-1].name}")
print(f"addr {info_list[-1].address}")
print(f"city {info_list[-1].location}")