arr = list(map(int, input().split()))


for i in range(3):
    if min(arr) < arr[i] and max(arr) > arr[i]:
        print(arr[i])