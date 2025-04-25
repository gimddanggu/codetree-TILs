m1, d1, m2, d2 = map(int, input().split())
A = input()

day_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_the_week = {
    "Mon": 0,
    "Tue": 1,
    "Wed": 2,
    "Thu": 3,
    "Fri": 4,
    "Sat": 5,
    "Sun": 6
}
day1, day2 = 0, 0

for i in range(m1):
    day1 += day_of_month[i]
for i in range(m2):
    day2 += day_of_month[i]

day1 += d1
day2 += d2

days_diff_idx = (day2 - day1) % 7 
days_diff_w = (day2 - day1) // 7

if day_of_the_week[A] <= days_diff_idx:
    print(days_diff_w + 1)
else :
    print(days_diff_w)


# Please write your code here.