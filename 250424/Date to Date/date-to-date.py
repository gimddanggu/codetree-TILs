m1, d1, m2, d2 = map(int, input().split())
m1Day, m2Day = 0, 0
month_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in range(m1+1):
    m1Day += month_day[i]
m1Day += d1

for i in range(m2+1):
    m2Day += month_day[i]
m2Day += d2

print(m2Day-m1Day)
# Please write your code here.
