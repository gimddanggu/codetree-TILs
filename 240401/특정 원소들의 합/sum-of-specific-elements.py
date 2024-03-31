arr2 = [list(map(int, input().split())) for _ in range(4)]
sum = 0

for k in range(4):
    for j in range(k, 4):
        sum += arr2[j][k]

print(sum)