subject = int(input())
score = list(map(float, input().split()))

score_avr = sum(score) / len(score)
print(f'{score_avr:.1f}')
if score_avr >= 4.0:
    print('Perfect')
elif score_avr >= 3.0:
    print('Good')
else:
    print('Poor')