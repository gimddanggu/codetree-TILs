arr = [list(map(int, input().split())) for _ in range(2)]
allsum = 0
# 가로 평균
for i in range(len(arr)):
    sumN = 0
    for j in range(len(arr[i])):
        sumN += int(arr[i][j])
    print(sumN / 4, end=' ')
print()

for j in range(4):
    verticalSum = arr[0][j] + arr[1][j]
    print( verticalSum / 2, end=' ')
    allsum += verticalSum
print()
print(f"{allsum / 8:.1f}")