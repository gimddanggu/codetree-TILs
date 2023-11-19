height, weight = map(int, input().split())

BMI = weight // (height**2) * 100**2
print(BMI)
if BMI >= 25:
    print('Obesity')