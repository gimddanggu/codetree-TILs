arr = list(map(int, input().split()))

cnt,arr_sum = 0, 0
for i in arr:
    if i == 0:
        break;
    cnt += 1
    arr_sum += i

print(arr_sum, round(arr_sum/cnt, 1))