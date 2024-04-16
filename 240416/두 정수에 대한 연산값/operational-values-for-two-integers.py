a, b = tuple(map(int, input().split()))

def sol(a, b):
    if a > b:
        a += 25
        b *= 2
    else:
        a *= 2
        b +=25
    return a, b


re1, re2 = sol(a, b)
print(re1, re2)