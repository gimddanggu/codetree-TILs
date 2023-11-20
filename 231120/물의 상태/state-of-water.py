temper = int(input())
state = ''
if temper < 0:
    state = 'ice'
elif temper < 100:
    state = 'water'
else:
    state = 'vapor'

print(state)