n = 5
data = []

class p:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} {self.height} {self.weight:.1f}"

for _ in range(n):
    n, h, w = input().split()
    data.append(p(n, int(h), float(w)))

name_sort_data = sorted(data, key=lambda x : x.name)
height_sort_data = sorted(data, key=lambda x : -x.height)

print("name")
for e in name_sort_data:
    print(e)
print()
print("height")
for e in height_sort_data:
    print(e)
# Please write your code here.