m1, d1, m2, d2 = map(int, input().split())
monthDay = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
# standard_day = d1 % 7 # 기준이 될 인덱스
# dayarr = [0] * 7

totalday1, totalday2 = 0, 0

# for i, val in enumerate(days):
#     print(i, val)
#     dayarr[(standard_day + i) % 7] = ((standard_day + i) % 7, val)

# 기준일로부터 며칠일 흘렀나?

for i in range(m1):
    totalday1 += monthDay[i]

for i in range(m2):
    totalday2 += monthDay[i]

totalday1 += d1
totalday2 += d2


# d1이 기준
# => d1 - d2 < 0 뒤의 날짜 
# => d1 - d2 > 0 앞선 날짜
resDay = totalday1 - totalday2
resIdx = abs(resDay) % 7



if resDay > 0: 
    print(days[-resIdx])

else:
    print(days[resIdx])
    