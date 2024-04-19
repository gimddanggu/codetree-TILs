def res1(n):
    if n == 0:
        return

    res1(n-1)
    print(n, end = ' ')

def res2(n):
    if n == 0:
        return 
    print(n, end =' ')
    res2(n-1)

    
n = int(input())
res1(n)
print()
res2(n)