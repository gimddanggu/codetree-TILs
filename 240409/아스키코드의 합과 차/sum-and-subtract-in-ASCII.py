a, b = tuple(map(ord, input().split()))

if b > a:
    a, b = b, a


plus, minus = a + b, a - b 
print(plus, minus)