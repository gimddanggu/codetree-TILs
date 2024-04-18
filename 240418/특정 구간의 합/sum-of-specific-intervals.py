n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))


def sol():
    result = 0
    a, b = tuple(map(int, input().split()))
    for i in range(a-1, b):
        result += arr[i]
    return result


for i in range(m):
    print(sol())