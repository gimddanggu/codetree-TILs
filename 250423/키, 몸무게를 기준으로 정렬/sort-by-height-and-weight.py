n = int(input())
data = []

class p:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def __str__(self):
        return f"{self.name} {self.height} {self.weight}"

for _ in range(n):
    n, h, w = input().split()
    data.append(p(n, int(h), int(w)))

data.sort(key=lambda x : (x.height, -x.weight))

for d in data:
    print(d)
# Please write your code here.