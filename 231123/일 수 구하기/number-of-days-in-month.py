n = int(input())
day31 = [1, 3, 5, 7, 8]
day30 = [4, 6, 9, 11]

if n == 2:
    day = 28
elif n in day31:
    day = 31
else:
    day = 30
print(day)