a, b, c = map(int,input().split())
min = 0

min = a if a <= b else b
min = min if min <= c else c

print(min)