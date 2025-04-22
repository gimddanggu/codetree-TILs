n = int(input())

data = []
class weatherD:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather
    
    def __str__(self):
        return f"{self.date} {self.day} {self.weather}"


def isRain(w):
    if w.weather == 'Rain':
        return 0, w.date
    return 1, w.date

for _ in range(n):
    data.append(weatherD(*input().split()))

data.sort(key=isRain)
print(data[0])
