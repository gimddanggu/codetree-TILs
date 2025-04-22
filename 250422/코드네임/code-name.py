MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

# Please write your code here.

class sol:
    def __init__(self, name, score):
        self.codename = name
        self.score = score

agents = []
for i in range(MAX_N):
    agents.append(sol(codenames[i], scores[i]))

# 객체는 만들었다.
# 클래스 정렬은 어떻게 하는지 모르겠다..
# 인덱스가 아니라 .멤버변수를 해주면 됐엇다.
agents.sort(key=lambda x : x.score)
print(agents[0].codename, agents[0].score)