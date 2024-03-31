n, m = tuple(map(int, input().split()))

arr_2d = [[i+(n-1)*j for i in range(1, m+1)] for j in range(n)]

for row in arr_2d:
    for elem in row:
        print(elem, end=' ')
    print()