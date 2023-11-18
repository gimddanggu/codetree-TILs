arr = [list(map(str, input().split())) for _ in range(5)]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = arr[i][j].upper()
        print(arr[i][j], end=' ')
    print()