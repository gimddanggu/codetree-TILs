arr = list(map(int, input().split()))

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        arr[i] //= 2
    else:
        arr[i] += 3

for ar in arr:
    if ar != 0:
        print(ar, end=' ')