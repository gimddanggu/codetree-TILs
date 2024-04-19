def re(n):
    if n == 0:
        return
        
    print('* ' * n)
    re(n-1)
    print("* " * n)


a = int(input())
re(a)