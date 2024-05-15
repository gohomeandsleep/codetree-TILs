class pcode:
    def __init__ (self, name ,code):
        self.name = name
        self.code = code
    
pcode1 = pcode("codetree", '50')
nm, cd = input().split()
pcode2 = pcode(nm, cd)

print(f"product {pcode1.code} is {pcode1.name}")
print(f"product {pcode2.code} is {pcode2.name}")