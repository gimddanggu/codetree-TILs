n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]
# 튜플은 수정(변경)이 불가능한 자료형이다.
# tuple(map(int, input().split())) + (i + 1,) 와 같은 방식은 새로운 요소를 추가하여 새로운 튜플을 만드는 것이다.


students.sort(key=lambda x : (-x[0], -x[1], x[2]))

for s in students:
    print(*s)
