def is_leap_year(y):
    if y % 4 != 0:
        return False
    # 이제 모두 4의 배수
    if y % 400 == 0:
        return True
    # 4의 배수이면서 400으로 안 나누어 떨어지는 수
    if y % 100 != 0:
        return True
    # 4의 배수이고 400으로 안 나누어 떨어지지만 100으로는 나누어 떨어지는 수

    return False

def m_last_date(y, m, d):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m == 2:
        if is_leap_year(y) :
            return 29
        return 28
    else:
        return 30

def w_season(m):
    if m <= 2 or m == 12:
        print('Winter')
    elif m < 6:
        print('Spring')
    elif m < 9:
        print('Summer')
    elif m < 12:
        print('Fall')
    
def is_date(y, m, d):
    if d <= m_last_date(y, m, d):
        w_season(m)
    else:
        print(-1)


a, b, c = tuple(map(int, input().split()))
#print(m_last_date(a, b, c))
is_date(a, b, c)