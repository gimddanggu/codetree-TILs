a, b, c = map(int, input().split())

# Please write your code here.
def calcDayTime(day, hour, minute):
    if (day < 11):
        return -1
    
    dayTmin = day * 24 * 60
    hourTmine = hour * 60
    return dayTmin + hourTmine + minute


# print(calcDayTime(11, 11, 11))
# print(calcDayTime(a, b, c))

print(calcDayTime(a, b, c) - calcDayTime(11, 11, 11))