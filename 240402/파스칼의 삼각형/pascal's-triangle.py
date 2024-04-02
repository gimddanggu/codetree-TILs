n = int(input())

arr_2d = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr_2d[j][0] = 1
    # arr_2d[i][i] = 1

 
for i in range(1, n):
    for j in range(1, n):
        arr_2d[i][j] = arr_2d[i-1][j-1] + arr_2d[i-1][j]


for row in arr_2d:
    for col in row:
        if col != 0:
            print(col, end=' ')
    print()