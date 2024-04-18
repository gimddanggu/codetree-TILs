n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))


def sol1(n, m):
    result = 0

    while(m >= 1):
        #print(arr[m-1])
        result += arr[m-1]
        if m % 2 != 0:
            m -= 1
        else:
            m //= 2

    return result


print(sol1(n, m))