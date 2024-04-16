n = int(input())
arr = list(map(int, input().split()))


def sol_abs(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] *= -1
            

sol_abs(arr)
for i in arr:
    print(i, end = ' ')