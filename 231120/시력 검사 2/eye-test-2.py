eyesight = float(input())
result = ''

if eyesight >= 1.0:
    result = 'High'

elif eyesight >= 0.5:
    result = 'Middle'
else:
    result = 'Low'

print(result)