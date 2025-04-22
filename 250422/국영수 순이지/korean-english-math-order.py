n = int(input())
name = []
korean = []
english = []
math = []
data = []
class pScore:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
    
    def __repr__(self):
        return f"{self.name} {self.korean} {self.english} {self.math}"

for _ in range(n):
    student_info = input().split()
    name = student_info[0]
    score = map(int, student_info[1:])
    data.append(pScore(name, *score))

data.sort(key=lambda x : (x.korean, x.english, x.math))

for i in data[::-1]:
    print(i)

# Please write your code here.