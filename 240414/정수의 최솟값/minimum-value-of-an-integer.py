def min_num(a, b, c):
    return min(a, b, c)


n1, n2, n3 = tuple(map(int, input().split()))
print(min_num(n1, n2, n3))