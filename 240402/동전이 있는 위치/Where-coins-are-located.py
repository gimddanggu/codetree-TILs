m, n = tuple(map(int, input().split()))
arr_2d = [[0] * m for _ in range(m)]

for i in range(n):
    a, b = tuple(map(int, input().split()))
    arr_2d[a-1][b-1] = 1
'''
for i in range(1, m+1):
    for j in range(1, m+1):
        print(arr_2d[i][j], end = ' ')
    print()
'''

'''
for row in arr_2d[1:m+1]:
    for col in row[1:m+1]:
        print(col, end = ' ')
    print()
'''

for row in arr_2d:
    for col in row:
        print(col, end = ' ')
    print()