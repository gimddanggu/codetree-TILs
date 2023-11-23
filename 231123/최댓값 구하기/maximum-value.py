a, b, c = map(int, input().split())
max = a

max = b if b > a else a
max = c if c > max else max

print(max)