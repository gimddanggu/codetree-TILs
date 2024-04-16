arr = list(map(int, input().split()))


def swap(arr):
    arr[0], arr[1] = arr[1], arr[0]

swap(arr)
for i in arr:
    print(i, end = ' ')