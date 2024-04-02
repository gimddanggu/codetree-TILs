m, n = tuple(map(int, input().split()))
arr_2d = [[0] * 10 for _ in range(10)]

for i in range(n):
    a, b = tuple(map(int, input().split()))
    arr_2d[a][b] = 1
'''
for i in range(1, m+1):
    for j in range(1, m+1):
        print(arr_2d[i][j], end = ' ')
    print()
'''

for row in arr_2d[1:m+1]:
    for col in row[1:m+1]:
        print(col, end = ' ')
    print()