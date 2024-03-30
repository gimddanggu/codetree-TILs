num = int(input())
arr = list(map(int, input().split()))

result_arr = [0 for _ in range(9)]

for elem in arr:
    result_arr[elem-1] += 1

for result in result_arr:
    print(result)