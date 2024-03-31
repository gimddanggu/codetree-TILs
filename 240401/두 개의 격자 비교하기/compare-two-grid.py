n, m = tuple(list(map(int, input().split())))
arr_2d1 = [list(map(int, input().split())) for _ in range(n)]
arr_2d2 = [list(map(int, input().split())) for _ in range(n)]

arr_2d3 = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr_2d1[i][j] != arr_2d2[i][j]:
            arr_2d3[i][j] = 1

for row in arr_2d3:
    for elem in row:
        print(elem, end = ' ')
    print()