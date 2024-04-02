n, m = tuple(map(int, input().split()))

# n*n 0으로 초기화 된 배열 생성
arr_2d = [[0]*n for _ in range(n)] 

for i in range(m):
    a, b = tuple(map(int, input().split()))
    arr_2d[a-1][b-1] = i+1

for row in arr_2d:
    for col in row:
        print(col, end = ' ')
    print()