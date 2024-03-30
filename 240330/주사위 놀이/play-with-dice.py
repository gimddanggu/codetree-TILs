arr = list(map(int, input().split()))

result_arr = [0 for _ in range(6)]

for elem in arr:
    result_arr[elem-1] += 1

for i in range(1,7):
    print(f"{i} - {result_arr[i-1]}")