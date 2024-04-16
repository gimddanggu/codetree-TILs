a, b = tuple(map(int, input().split()))


def sol_date(m, d):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        if d <= 31:
            return True
    
    elif m == 2:
        if d <= 28:
            return True

    else:
        if d <= 30:
            return True
    
    return False


if sol_date(a, b):
    print('Yes')
else:
    print('No')