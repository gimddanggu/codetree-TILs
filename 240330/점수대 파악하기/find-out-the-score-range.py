arr = list(map(int, input().split()))

cnt_arr = [0]*11

for elem in arr:
    if elem != 100:
        cnt_arr[elem // 10] += 1
    elif elem == 100:
        cnt_arr[10] += 1

for i in range(10, 0, -1):
    print(f"{i*10} - {cnt_arr[i]}")