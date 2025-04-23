n = int(input())
students = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]
# 키, 몸무게, 번호
students.sort(key=lambda x : -x[1])
students.sort(key=lambda x : x[0])

for s in students:
    print(*s)

# Please write your code here.