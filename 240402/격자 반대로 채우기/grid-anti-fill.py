n = int(input())
num = 1
arr_2d = [[0 for _ in range(n)] for _ in range(n)]


for i in range(n-1, -1, -1):
    if n % 2 != 0 and i % 2 == 0 or n % 2 == 0 and i % 2 != 0: 
        for j in range(n-1, -1, -1):
            #print(f"i: {i} j: {j}")
            arr_2d[j][i] = num
            num += 1
    if n % 2 != 0 and i % 2 != 0 or n % 2 == 0 and i % 2 == 0:
        for j in range(n):
            #print(f"i: {i} j: {j}")
            arr_2d[j][i] = num
            num += 1


for row in arr_2d:
    for col in row:
        print(col, end = ' ')
    print()
#print(arr_2d)