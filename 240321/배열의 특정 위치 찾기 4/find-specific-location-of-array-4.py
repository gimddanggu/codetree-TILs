arr = list(map(int, input().split()))

cnt, arr_sum = 0, 0
for i in arr:
    if i == 0:
        break;
    if i % 2 == 0:
        cnt += 1
        arr_sum += i

print(f"{cnt} {arr_sum}")