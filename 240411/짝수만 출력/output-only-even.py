a, b = tuple(map(int, input().split()))

while(a <= b):
    if a % 2 == 0:
        print(a, end =' ')
        a += 2
    else:
        a += 1