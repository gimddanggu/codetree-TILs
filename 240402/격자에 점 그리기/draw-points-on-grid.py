n, m = tuple(map(int, input().split()))

# n*n 0으로 초기화 된 배열 생성
arr_2d = [[0]*10 for _ in range(10)] 

for i in range(1, m+1):
    a, b = tuple(map(int, input().split()))
    arr_2d[a][b] = i

for i in range(1,n+1):
    for j in range(1, n+1):
        print(arr_2d[i][j], end = ' ')
    print()