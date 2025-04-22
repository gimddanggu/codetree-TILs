n = int(input())
data = []

class sol:

    def __init__(self, name, s1, s2, s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
    
    def __str__(self):
        return f"{self.name} {self.s1} {self.s2} {self.s3}"

for i in range(n):
    student_input = input().split()
    name = student_input[0]
    Scores = list(map(int, student_input[1:])) # map 은 이터레이터(한 번만 소비 가능한 객체)
    data.append(sol(name, *Scores))          # map 결과를 변수로 저장하면 다음 호출 할 때 값이 없음
    sumScore = sum(Scores)
    data[i].sSum = sumScore

data.sort(key=lambda x : x.sSum)
for i in data:
    print(i)
# Please write your code here.