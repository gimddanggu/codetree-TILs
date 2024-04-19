def rs(n):
    if n == 0:
        return

    print(n, end = ' ')
    rs(n-1)
    print(n, end = ' ')


a = int(input())
rs(a)