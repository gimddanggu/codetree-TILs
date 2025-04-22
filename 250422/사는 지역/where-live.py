n = int(input())

class_arr = []

class sol:
    def __init__(self, name, addr, reg):
        self.name = name
        self.addr = addr
        self.reg = reg

    def __str__(self):
        return f"name {self.name}\naddr {self.addr}\ncity {self.reg}"


for _ in range(n):
    # 객체 초기화
    class_arr.append(sol(*input().split()))

class_arr.sort(key=lambda x : x.name)
print(class_arr[-1])

