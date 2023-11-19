height, weight = map(int, input().split())

BMI = weight * 100**2 // (height**2) 
print(BMI)
if BMI >= 25:
    print('Obesity')