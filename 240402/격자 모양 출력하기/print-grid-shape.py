n, m = tuple(map(int, input().split()))

arr_2d = [[0]*n for _ in range(n)]

for _ in range(m):
    a, b = tuple(map(int, input().split()))
    arr_2d[a-1][b-1] = a * b
'''
for row in arr_2d:
    for col in row:
        print(col, end=' ')
    print()
    '''
for i in range(n):
	for j in range(n):
		print(arr_2d[i][j], end=" ")
	print()