rs = float(input())
ls = float(input())


if rs >= 1.0 and ls >= 1.0:
    print('High')
elif rs >= 0.5 and ls >= 0.5:
    print('Middle')
else:
    print('Low')