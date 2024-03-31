n, m = tuple(map(int, input().split()))

arr_2d = [[i+m*j for i in range(1, m+1)] for j in range(n)]

for row in arr_2d:
    for elem in row:
        print(elem, end=' ')
    print()