n, m = tuple(map(int, input().split()))

arr_2d = [[0 for _ in range(m)] for _ in range(n)] # 2차원 0 배열 생성


num = 0
for i in range(n):
    arr_2d[i][0] = num
    num += 1


for i in range(1, m):
    
    if i % 2 == 0: # 인덱스 홀수열
        for j in range(n):
            arr_2d[j][i] = num
            num += 1
            #print(f"ej: {j} i: {i}")
            
    else: # 인덱스 짝수열
        for j in range(n-1,-1,-1):
            arr_2d[j][i] = num
            num += 1
            #print(f"j: {j} i: {i}")


for row in arr_2d:
    for elem in row:
        print(elem, end=' ')
    print()