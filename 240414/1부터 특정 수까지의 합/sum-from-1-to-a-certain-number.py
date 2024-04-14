def func(a):
    sum_n = 0
    for i in range(1, a+1):
        sum_n += i
    result = sum_n // 10
    return result


n = int(input())
print(func(n))