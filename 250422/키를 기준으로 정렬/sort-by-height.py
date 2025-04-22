n = int(input())
data = []
class person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height    
        self.weight = weight

    def __repr__(self):
        return f"{self.name} {self.height} {self.weight}"

for _ in range(n):
    data.append(person(*input().split()))
        
sorted_data = sorted(data, key=lambda x: x.height)
for i in range(n):
    print(sorted_data[i])


# Please write your code here.