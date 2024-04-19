def res(n):
    if n == 0:
        return

    res(n-1)
    print('*'*n)
    

a = int(input())
res(a)