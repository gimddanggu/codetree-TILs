def func(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return n + func(n-2)


N = int(input())
print(func(N))